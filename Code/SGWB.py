import matplotlib.pyplot as plt
import numpy as np
import os

def plot_fig5_sgwb_official():
    """
    生成 FIG. 5: 颜色完全对齐论文描述
    - Omega-TSCI (nT = -0.49): 红色 (Red)
    - Standard Inflation (nT = 0): 蓝色 (Blue)
    - LiteBIRD Zone: 灰色/紫色阴影
    """
    f = np.logspace(-18, -1, 300)
    gamma = 0.4977
    nT_tsci = 1 - 3 * gamma  # 约为 -0.49
    
    # 1. 能谱数据计算
    # Omega-TSCI (红色)
    Omega_tsci = 1e-15 * (f / 1e-16)**nT_tsci
    # 标准暴胀 (蓝色, nT ≈ 0, 设为平直谱)
    Omega_infl = 1e-15 * (f / 1e-16)**0 

    # 2. 样式设置
    plt.rcParams.update({
        "font.family": "serif",
        "mathtext.fontset": "cm",
        "font.size": 12,
        "figure.dpi": 300
    })
    plt.figure(figsize=(8, 6))

    # 3. 绘制曲线
    # Omega-TSCI -> 红色实线
    plt.loglog(f, Omega_tsci, color='#d62728', lw=2.5, 
               label=r'$\Omega$-TSCI Prediction ($n_T = -0.49$)')
    
    # Standard Inflation -> 蓝色虚线 (对比项)
    plt.loglog(f, Omega_infl, color='#1f77b4', lw=2, linestyle='--',
               label=r'Standard Inflation ($n_T \approx 0$)')

    # 4. LiteBIRD 敏感区 -> 阴影 (改用中性颜色避免混淆)
    plt.fill_between([1e-18, 1e-16], 1e-17, 1e-13, 
                     color='purple', alpha=0.1, label='LiteBIRD Sensitivity Zone')

    # 5. 装饰与标注
    plt.xlabel("Frequency $f$ (Hz)", fontsize=13)
    plt.ylabel(r"Energy Density $\Omega_{GW}(f)$", fontsize=13)
    plt.title("FIG 5. Predicted SGWB Spectrum", fontsize=14, pad=15)
    
    plt.xlim(1e-19, 1e-1)
    plt.ylim(1e-22, 1e-12)
    plt.grid(True, which="both", ls="-", alpha=0.15)
    plt.legend(loc='upper right', frameon=True)

    # 6. 保存
    os.makedirs("visualizations", exist_ok=True)
    plt.tight_layout()
    plt.savefig("visualizations/fig5_sgwb_final.png")
    plt.show()

if __name__ == "__main__":
    plot_fig5_sgwb_official()
