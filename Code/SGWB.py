import matplotlib.pyplot as plt
import numpy as np
import os

def plot_fig5_sgwb_official_v2():
    """
    生成 FIG. 5: 严格对齐 gamma = 0.4933 导出的 nT = -0.48
    - Omega-TSCI (nT = -0.48): 红色 (Red)
    - Standard Inflation (nT = 0): 蓝色 (Blue)
    - 导出逻辑: nT = 1 - 3gamma (不再依赖 alpha_eff)
    """
    f = np.logspace(-18, -1, 300)
    gamma = 0.4933
    # 核心计算：1 - 3*0.4933 = -0.4799，取两位小数为 -0.48
    nT_tsci = -0.48  
    
    # 1. 能谱数据计算
    # Omega-TSCI (红色实线)
    Omega_tsci = 1e-15 * (f / 1e-16)**nT_tsci
    # 标准暴胀 (蓝色虚线, nT ≈ 0)
    Omega_infl = 1e-15 * (f / 1e-16)**0 

    # 2. 样式设置 (保持 1200 DPI 高清输出)
    plt.rcParams.update({
        "font.family": "serif",
        "mathtext.fontset": "cm",
        "font.size": 12,
        "figure.dpi": 1200
    })
    plt.figure(figsize=(8, 6))

    # 3. 绘制曲线
    # Omega-TSCI -> 红色实线
    plt.loglog(f, Omega_tsci, color='#d62728', lw=2.5, 
               label=r'$\Omega$-TSCI Prediction ($n_T = -0.48$)')
    
    # Standard Inflation -> 蓝色虚线
    plt.loglog(f, Omega_infl, color='#1f77b4', lw=2, linestyle='--',
               label=r'Standard Inflation ($n_T \approx 0$)')

    # 4. LiteBIRD 敏感区 (保持紫色阴影)
    plt.fill_between([1e-18, 1e-16], 1e-17, 1e-13, 
                     color='purple', alpha=0.1, label='LiteBIRD Sensitivity Zone')

    # 5. 装饰与标注
    plt.xlabel("Frequency $f$ (Hz)", fontsize=13)
    plt.ylabel(r"Energy Density $\Omega_{GW}(f)$", fontsize=13)
    # 标题建议改为更正式的表述
    plt.title(r"FIG 5. SGWB Power Spectrum Predicted by $\gamma=0.4933$", fontsize=14, pad=15)
    
    plt.xlim(1e-19, 1e-1)
    plt.ylim(1e-22, 1e-12)
    plt.grid(True, which="both", ls="-", alpha=0.15)
    plt.legend(loc='upper right', frameon=True)

    # 6. 保存到指定文件夹
    os.makedirs("visualizations", exist_ok=True)
    plt.tight_layout()
    plt.savefig("visualizations/fig5_sgwb_final_048.png")
    plt.show()

if __name__ == "__main__":
    plot_fig5_sgwb_official_v2()
