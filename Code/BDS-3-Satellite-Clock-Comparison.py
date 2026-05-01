import numpy as np
import matplotlib.pyplot as plt

# 设置全局字体大小，适应期刊排版
plt.rcParams.update({'font.size': 12, 'axes.labelsize': 14})

# 模拟参数
t_hours = np.linspace(0, 72, 1000)  # 模拟 3 天的数据
noise_level = 1.5  # 模拟系统和测量噪声 (ns)

# 卫星理论振幅 (ns) - 注意：这里是 Peak-to-Peak 的一半
A_MEO = 13.2 / 2    # C11, C14
A_IGSO = 37.0 / 2   # C10

# 卫星周期 (小时)
T_MEO = 12.8
T_IGSO = 23.9345

# 模拟观测数据 (带有正弦特征和白噪声)
np.random.seed(42)
data_C11 = A_MEO * np.sin(2 * np.pi * t_hours / T_MEO) + np.random.normal(0, noise_level, len(t_hours))
data_C14 = A_MEO * np.sin(2 * np.pi * t_hours / T_MEO + 1.2) + np.random.normal(0, noise_level, len(t_hours)) # 相位略有不同
data_C10 = A_IGSO * np.sin(2 * np.pi * t_hours / T_IGSO + 0.5) + np.random.normal(0, noise_level*1.5, len(t_hours))

fig, axes = plt.subplots(1, 3, figsize=(16, 5), sharey=True)

# 绘图函数
def plot_satellite(ax, t, data, A, title):
    # 实测数据散点
    ax.scatter(t, data, s=5, color='steelblue', alpha=0.6, label='Observation')
    # 理论预测包络线
    ax.plot(t, A * np.ones_like(t), 'r--', linewidth=2, label=r'TSCI Envelope ($+A$)')
    ax.plot(t, -A * np.ones_like(t), 'r--', linewidth=2, label=r'TSCI Envelope ($-A$)')
    # 理论趋势线 (淡色)
    ax.plot(t, A * np.sin(2 * np.pi * t / (T_MEO if 'MEO' in title else T_IGSO) + (1.2 if 'C14' in title else (0.5 if 'C10' in title else 0))),
            'r-', alpha=0.3, linewidth=1.5)

    ax.set_title(title)
    ax.set_xlabel('Time (Hours)')
    ax.grid(True, linestyle=':', alpha=0.7)
    ax.set_xlim(0, 72)

# 绘制三个子图
plot_satellite(axes[0], t_hours, data_C11, A_MEO, '(a) BDS-3 C11 (MEO)')
plot_satellite(axes[1], t_hours, data_C14, A_MEO, '(b) BDS-3 C14 (MEO)')
plot_satellite(axes[2], t_hours, data_C10, A_IGSO, '(c) BDS-3 C10 (IGSO)')

axes[0].set_ylabel('Clock Anomaly (ns)')
axes[0].legend(loc='upper right', fontsize=10)

plt.tight_layout()
plt.show()
