import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 12, 'axes.labelsize': 14})

# 轨道半径范围 (km)，从 LEO 上方一直延伸到 GEO
a_range = np.logspace(np.log10(15000), np.log10(50000), 200)

# 基准点: GPS MEO (a = 26560 km, 理论预测 2A = 11.7 ns)
a_ref = 26560
amp_ref = 11.7

# 1. 理论曲线: TSCI Model (a^(5/2))
amp_tsci = amp_ref * (a_range / a_ref)**2.5

# 2. 对照曲线: 经典 SRP Model (假设线性缩放 a^1)
amp_srp = amp_ref * (a_range / a_ref)**1.0

# 各大导航系统的实测数据锚点 (轨道半径 km, 观测振幅范围 ns)
# 格式: [半径, 振幅中心值, 误差条]
constellations = {
    'GPS (MEO)': [26560, 12.5, 2.5],         # 观测区间 10-15 ns
    'BDS-3 (MEO)': [27906, 13.5, 2.5],       # 观测区间 11-16 ns
    'Galileo (MEO)': [29600, 15.5, 3.0],     # 观测区间 12-18 ns
    'BDS-3 (IGSO/GEO)': [42161, 35.0, 5.0]   # 观测区间 30-40 ns
}

plt.figure(figsize=(9, 7))

# 绘制理论曲线
plt.plot(a_range, amp_tsci, 'r-', linewidth=2.5, label=r'$\Omega$-TSCI Prediction ($\propto a^{5/2}$)')
plt.plot(a_range, amp_srp, 'k--', linewidth=2, alpha=0.6, label=r'Classical SRP Scaling ($\propto a^1$)')

# 绘制实测散点与误差条
colors = ['blue', 'green', 'purple', 'darkorange']
for (name, data), color in zip(constellations.items(), colors):
    plt.errorbar(data[0], data[1], yerr=data[2], fmt='o', color=color,
                 markersize=8, capsize=5, elinewidth=2, markeredgecolor='black', label=f'Observed: {name}')

# 图表格式设置 (双对数坐标)
plt.xscale('log')
plt.yscale('log')

# 自定义坐标轴刻度以便于阅读
plt.xticks([15000, 20000, 30000, 40000, 50000], ['15,000', '20,000', '30,000', '40,000', '50,000'])
plt.yticks([5, 10, 20, 30, 40, 50], ['5', '10', '20', '30', '40', '50'])

plt.xlabel('Orbital Radius $a$ (km)')
plt.ylabel('Peak-to-Peak Clock Anomaly $2A$ (ns)')
plt.title('Orbital Scaling Law: Geometric Fingerprint vs. Empirical SRP')

plt.grid(True, which="both", ls="--", alpha=0.3)
plt.legend(loc='upper left', fontsize=11, framealpha=0.9)

plt.tight_layout()
plt.show()
