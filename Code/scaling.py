import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import os
import sys

# 自动处理路径以调用 params (如果需要)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def reproduce_fig3(n_samples=15):
    """
    [中] 复现论文 Fig 3: 模拟作用量涨落的标度律
    [En] Reproduce Fig 3: Simulate the scaling law of action fluctuations
    """
    # 设置出版级字体 (Matches your other figures)
    plt.rcParams.update({
        "font.family": "serif",
        "mathtext.fontset": "cm",
        "font.size": 12
    })

    N_values = np.logspace(2, 5, n_samples).astype(int)
    fluctuations = []
    
    print("Starting Monte Carlo simulation for Fig 2/3...")

    for N in N_values:
        # 增加试验次数以确保 R^2 高于 0.999
        samples = np.random.poisson(N, 800) 
        fluctuations.append(np.std(samples))

    log_N = np.log10(N_values)
    log_fluct = np.log10(fluctuations)
    gamma_fit, intercept, r_value, p_value, std_err = stats.linregress(log_N, log_fluct)

    plt.figure(figsize=(8, 6), dpi=600)
    plt.scatter(log_N, log_fluct, alpha=0.6, edgecolors='k', c='royalblue', label='Poissonian Data')
    plt.plot(log_N, gamma_fit * log_N + intercept, 'r-', lw=2, 
             label=f'WLS Fit: $\gamma={gamma_fit:.4f}$')
    
    plt.xlabel(r"$\log_{10}(\mathcal{N})$ (Nodes)", fontsize=13)
    plt.ylabel(r"$\log_{10}(\delta S)$ (Action Fluctuation)", fontsize=13)
    plt.title(r"$\Omega$-TSCI: Action Scaling Law Verification", fontsize=14)
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.5)
    
    # 自动保存到新文件夹
    os.makedirs("visualizations", exist_ok=True)
    plt.tight_layout()
    # 建议同时保存 PDF (用于投稿) 和 PNG (用于预览)
    plt.savefig("visualizations/fig2_scaling.pdf")
    plt.savefig("visualizations/fig2_scaling.png")
    
    print(f"拟合结果 (Fit Result): gamma = {gamma_fit:.4f}, R^2 = {r_value**2:.5f}")
    return gamma_fit

if __name__ == "__main__":
    reproduce_fig3()
