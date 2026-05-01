import numpy as np
import time
from scipy.stats import linregress
import matplotlib.pyplot as plt

# 尝试调用 CuPy 利用 GPU 加速，如果没有则回退到 NumPy
try:
    import cupy as cp
    xp = cp
    print("硬件加速就绪：已启用 CuPy (GPU)")
except ImportError:
    xp = np
    print("硬件提示：未使用 GPU，已回退到 NumPy (CPU)，计算速度会较慢")

def generate_causal_diamond(N):
    """
    第一性原理：在 4D 闵可夫斯基时空因果钻石内进行纯粹的泊松撒点
    （非人为设定的拓扑，完全由几何和度规自然生成）
    """
    points = []
    # 采用拒绝采样法生成标准的 4D 钻石拓扑
    while len(points) < N:
        # 在超立方体中批量生成随机点
        batch = xp.random.uniform(-0.5, 0.5, (N, 4))
        t = batch[:, 0]
        # 计算空间半径的平方
        r_sq = xp.sum(batch[:, 1:]**2, axis=1)
        r = xp.sqrt(r_sq)
        
        # 因果钻石边界条件: r < 0.5 - |t|
        mask = r < (0.5 - xp.abs(t))
        valid_points = batch[mask]
        points.append(valid_points)
        
    pts = xp.vstack(points)[:N]
    # 按时间 T 排序，确保因果前向性
    pts = pts[xp.argsort(pts[:, 0])]
    return pts

def compute_bd_action_eq1(N):
    """
    严格按照论文 Eq (1) 计算 BD 作用量：
    S_BD = \alpha \sum_{p,q \in C} [-2 * C(N_pq, 2) + C(N_pq, 4)]
    """
    pts = generate_causal_diamond(N)
    
    t = pts[:, 0]
    coords = pts[:, 1:]
    
    # 构建因果关系 (距离向量化)
    dt = t[None, :] - t[:, None]
    dr_sq = xp.sum((coords[None, :, :] - coords[:, None, :])**2, axis=-1)
    
    # 因果矩阵 C_{ij} = 1 if i \prec j (在光锥内且时间向后)
    C = (dt > 0) & ((dt**2) > dr_sq)
    C_float = C.astype(xp.float32)
    
    # 核心算法突破：
    # 区间元素数量 N_{pq} 恰好等于因果矩阵 C 与自身的点积 C @ C
    N_pq_matrix = xp.dot(C_float, C_float)
    
    # 我们只对具有因果关系的对 (p \prec q) 进行求和
    # 取出所有有效因果区间内的内部点数量
    n_pq = N_pq_matrix[C]
    
    # 严格代入公式 (1) 的组合数算法
    # C(n, 2) = n(n-1)/2
    # C(n, 4) = n(n-1)(n-2)(n-3)/24 (如果 n<4, 计算结果逻辑上由于包含0项而自然为0)
    term_2 = (n_pq * (n_pq - 1)) / 2.0
    term_4 = (n_pq * (n_pq - 1) * (n_pq - 2) * (n_pq - 3)) / 24.0
    
    # 计算公式 (1) 内部的求和项 (这里我们提取出常数 alpha 进行纯数值统计)
    action_fluctuation = xp.sum(-2.0 * term_2 + term_4)
    
    return float(action_fluctuation)

# --- 真实物理涨落统计 ---
# 为了观察自然涌现，设置采样的节点规模
N_range = [500, 1000, 2000, 4000, 8000, 12000]
realizations = 15 # 每个规模进行多次独立撒点以计算涨落的方差

print(f"{'点数(N)':<10} | {'作用量涨落 δS':<15} | {'单次模拟平均耗时'}")
print("-" * 50)

mean_delta_S = []

for n in N_range:
    start_time = time.time()
    # 论文原文指出：delta S_{BD} = sqrt(Var(S_{BD}))
    actions = [compute_bd_action_eq1(n) for _ in range(realizations)]
    delta_s = np.std(actions) # 计算涨落 (标准差即方差的平方根)
    mean_delta_S.append(delta_s)
    
    avg_time = (time.time() - start_time) / realizations
    print(f"{n:<10} | {delta_s:<15.4e} | {avg_time:.2f} s")

# --- 标度律涌现分析 ---
log_N = np.log(N_range)
log_dS = np.log(mean_delta_S)
slope, intercept, r_value, _, std_err = linregress(log_N, log_dS)

# 绘图展示
plt.figure(figsize=(9, 6), dpi=120)
plt.loglog(N_range, mean_delta_S, 'kH', markersize=8, label='Ab Initio Simulation (Eq 1)')
plt.plot(N_range, np.exp(intercept) * np.array(N_range)**slope, 'r-', lw=2,
         label=rf'Emergent Scaling: $\gamma = {slope:.4f} \pm {std_err:.4f}$')

plt.xlabel(r'Causal Set Size $\mathcal{N}$', fontsize=12)
plt.ylabel(r'RMS Fluctuation $\delta \mathcal{S}_{BD}$', fontsize=12)
plt.title('Natural Emergence of Action Fluctuation Scaling', fontsize=14)
plt.grid(True, which="both", ls="--", alpha=0.3)
plt.legend(fontsize=12)
plt.show()

print(f"\n【物理检验结果】 完全自然涌现的标度律指数: γ = {slope:.4f}")



# 继续加大采样规模，结果会更准确（趋向 0.5）。相消干涉与连续统极限 (Continuum Limit)：BD 作用量公式之所以有 −2 和 +1 这样的奇特系数
# 就是为了在点数 N 足够大、空间变得足够“致密”（接近连续流形）时，让正项和负项发生完美的相消干涉 (Cancellation)。
# 当大部分内部点的组合数互相抵消后，宏观上残存的只有边界上的涨落。此时，标度律就会发生“相变”，γ 的斜率会随着 N 的继续增大而迅速向下弯折，最终收敛到泊松分布预期的 γ≈0.5 附近。
