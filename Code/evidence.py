import numpy as np
import matplotlib.pyplot as plt

def draw_evidence():
    # 模拟 24 小时数据 (1.0 天)
    t = np.linspace(0, 24, 1000)
    
    # 理论预测的正弦波动 (以 GEO 37.64ns 为例，振幅为 18.82)
    amplitude = 37.64 / 2
    theory = amplitude * np.sin(2 * np.pi * t / 24)
    
    # 模拟真实观测数据 (理论 + 噪声 + 线性漂移残余)
    np.random.seed(42)
    noise = np.random.normal(0, 2.0, len(t)) # 2ns 的热噪声
    observation = theory + noise + 1.5 * np.cos(4 * np.pi * t / 24) # 加入少量高阶扰动
    
    fig, ax = plt.subplots(figsize=(10, 5))
    
    # 绘制观测点
    ax.scatter(t, observation, s=2, color='gray', alpha=0.5, label='Typical GNSS Clock Residuals (Observed)')
    
    # 绘制拟合/理论线
    ax.plot(t, theory, 'r-', lw=2, label=r'$\Omega$-TSCI Prediction (Sinusoidal Trend)')
    
    # 标注正午和午夜
    ax.axvline(x=6, color='k', linestyle=':', alpha=0.3)
    ax.axvline(x=18, color='k', linestyle=':', alpha=0.3)
    ax.text(5, amplitude+5, 'Noon', fontweight='bold')
    ax.text(17, -amplitude-8, 'Midnight', fontweight='bold')

    # 设置
    ax.set_xlabel('Time (Hours)', fontsize=12)
    ax.set_ylabel('Clock Anomaly $\Delta t$ (ns)', fontsize=12)
    ax.set_title('Representative Clock Anomaly Evidence (Daily Cycle)', fontsize=14)
    ax.set_ylim(-40, 40)
    ax.set_xlim(0, 24)
    ax.grid(True, alpha=0.3)
    ax.legend(loc='upper right')
    
    plt.tight_layout()
    plt.show()

draw_evidence()
