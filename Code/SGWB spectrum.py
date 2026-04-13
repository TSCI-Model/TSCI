import matplotlib.pyplot as plt
import numpy as np
import os

def plot_gw_spectrum():
    """
    预言随机引力波背景 (SGWB) 能谱 - PRD 优化版
    Predict the SGWB spectrum - Optimized for PRD publication
    """
    # 1. 物理参数定义 (Physical Parameters)
    f = np.logspace(-18, -1, 100)  # 频率范围
    gamma = 0.4977
    nT = 1 - 3 * gamma             # 理论推导: nT ≈ -0.49
    f_H = 2.3e-18                  # 当前哈勃频率参考值 (Hz)
    
    # 能谱密度 (Energy density scaling)
    # 基于 A_tsci ≈ 1e-15 的基准强度
    Omega_gw = 1e-15 * (f / 1e-16)**nT
    
    # 2. 设置出版级绘图样式 (Publication Style)
    plt.rcParams.update({
        "font.family": "serif",
        "mathtext.fontset": "cm",
        "font.size": 12,
        "figure.dpi": 300
    })

    plt.figure(figsize=(9, 6.5))
    
    # 3. 绘制主曲线 (Plot Prediction)
    plt.loglog(f, Omega_gw, color='#1f77b4', lw=2.5, 
               label=r'$\Omega$-TSCI Prediction ($n_T \approx %.2f$)' % nT)
    
    # 4. 绘制检测器敏感区 (LiteBIRD Sensitivity Zone)
    # 优化了阴影的视觉效果
    plt.fill_between([1e-18, 1e-16], 1e-17, 1e-13, 
                     color='#1f77b4', alpha=0.15, label='LiteBIRD Sensitivity Zone')
    
    # 5. 新增：标注哈勃频率参考线 (Hubble Frequency Reference)
    plt.axvline(x=f_H, color='gray', linestyle='--', alpha=0.6, lw=1.2)
    plt.text(f_H * 1.2, 1e-20, r'$f_H$', fontsize=14, color='gray')
    
    # 6. 图表装饰 (Formatting)
    plt.title("Stochastic Gravitational Wave Background", fontsize=14, pad=15)
    plt.xlabel("Frequency $f$ (Hz)", fontsize=13)
    plt.ylabel(r"Energy Density $\Omega_{GW}(f)$", fontsize=13)
    
    plt.legend(loc='upper right', frameon=True, fancybox=True, framealpha=0.9)
    plt.grid(True, which="both", ls="-", alpha=0.2)
    
    # 限制坐标轴范围，使视觉重心集中在预言区
    plt.ylim(1e-22, 1e-12)
    
    # 7. 导出与显示 (Export)
    os.makedirs("visualizations", exist_ok=True)
    plt.tight_layout()
    plt.savefig("visualizations/fig5_sgwb_optimized.pdf", bbox_inches='tight')
    plt.savefig("visualizations/fig5_sgwb_optimized.png", bbox_inches='tight')
    
    print(f"✅ 图表已优化并保存至: visualizations/fig5_sgwb_optimized.png")
    plt.show()

if __name__ == "__main__":
    plot_gw_spectrum()
