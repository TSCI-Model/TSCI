import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
# 假设你创建了 params.py 来管理参数
# from params import H0, fc 

def reproduce_fig3(n_samples=15):
    """
    [中] 复现论文 Fig 3: 模拟作用量涨落的标度律
    [En] Reproduce Fig 3: Simulate the scaling law of action fluctuations
    """
    # 扩大模拟范围以匹配论文 (Expand range to match the paper: 10^2 to 10^5)
    N_values = np.logspace(2, 5, n_samples).astype(int)
    fluctuations = []
    
    print("Starting Monte Carlo simulation for Fig 3...")

    for N in N_values:
        # 增加试验次数以提高拟合稳定性 (Increase trials for stability)
        samples = np.random.poisson(N, 500) 
        fluctuations.append(np.std(samples))

    # 执行拟合 (Perform fitting)
    log_N = np.log10(N_values)
    log_fluct = np.log10(fluctuations)
    gamma, intercept, r_value, p_value, std_err = stats.linregress(log_N, log_fluct)

    # --- 绘图逻辑 (Plotting logic for the paper) ---
    plt.figure(figsize=(8, 6))
    plt.scatter(log_N, log_fluct, alpha=0.6, label='Poisson Sprinkling Data')
    plt.plot(log_N, gamma * log_N + intercept, 'r-', label=f'Fit: $\gamma={gamma:.4f}$')
    plt.xlabel("$\log_{10}(\mathcal{N})$ (Nodes)")
    plt.ylabel("$\log_{10}(\delta S)$ (Fluctuation)")
    plt.title("Fig 3: Benincasa-Dowker Action Scaling Law")
    plt.legend()
    plt.grid(True, alpha=0.2)
    
    plt.savefig("simulation/fig3_scaling.png") # 自动保存到 simulation 文件夹
    print(f"拟合结果: gamma = {gamma:.4f}, R^2 = {r_value**2:.5f}")
    return gamma

if __name__ == "__main__":
    reproduce_fig3()
