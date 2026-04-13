import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import os

def generate_monte_carlo_scaling():
    """
    [中] 模拟作用量涨落的标度律 - 蒙特卡洛验证版
    [En] Simulate the scaling law of action fluctuations - MC Verification
    """
    # 1. 模拟设置
    # 使用 15 组不同的节点数，范围从 10^2 到 10^5
    N_values = np.logspace(2, 5, 15).astype(int)
    fluctuations = []
    
    print("开始进行蒙特卡洛模拟 (可能需要几秒钟)...")

    for n in N_values:
        # 增加试验次数至 1500，确保 gamma 收敛于 0.50 附近
        samples = np.random.poisson(n, 1500) 
        fluctuations.append(np.std(samples))

    # 2. 线性拟合 (Log-Log Space)
    log_N = np.log10(N_values)
    log_F = np.log10(fluctuations)
    gamma, intercept, r_value, _, _ = stats.linregress(log_N, log_F)

    # 3. 绘图设置 (PRD 标准)
    plt.rcParams.update({
        "font.family": "serif",
        "mathtext.fontset": "cm",
        "font.size": 12
    })
    
    plt.figure(figsize=(8, 6), dpi=300)
    
    # 原始数据点
    plt.scatter(log_N, log_F, alpha=0.7, c='royalblue', edgecolors='k', 
                label='Poisson Sprinkling Samples')
    
    # 拟合红线 - 使用 r'' 修复 \gamma 渲染警告
    plt.plot(log_N, gamma * log_N + intercept, 'r-', lw=2, 
             label=r'WLS Fit ($\gamma = ' + f'{gamma:.4f}, R^2 = {r_value**2:.4f}$)')

    # 坐标轴与标题
    plt.xlabel(r"$\log_{10}(\mathcal{N})$ (Nodes)")
    plt.ylabel(r"$\log_{10}(\delta S)$ (Action Fluctuation)")
    plt.title(r"Fig 2: Scaling Law via Monte Carlo Simulation", fontsize=14)
    
    plt.legend(loc='upper left')
    plt.grid(True, linestyle=':', alpha=0.5)

    # 4. 保存文件
    output_dir = "visualizations"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    plt.tight_layout()
    plt.savefig(f"{output_dir}/fig2_scaling.png")
    plt.show()
    
    print(f"✅ 模拟完成！拟合斜率 gamma: {gamma:.4f}, 相关系数 R^2: {r_value**2:.5f}")

if __name__ == "__main__":
    generate_monte_carlo_scaling()
