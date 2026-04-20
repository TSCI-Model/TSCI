import numpy as np
import matplotlib.pyplot as plt

# --- 物理常数定义 (源自论文 .tex) ---
gamma = 0.4933      # 拓扑常数
gs = 0.005930       # 太阳引力加速度 (m/s^2)
c = 299792458.0     # 光速 (m/s)
GMe = 3.986004418e14 # 地球引力常数

def calculate_tsci_pp(R_km):
    """计算 Ω-TSCI 模型的峰峰值 (ns)"""
    R = R_km * 1000
    # 角速度 omega = sqrt(GM/R^3)
    omega = np.sqrt(GMe / R**3)
    # 峰峰值公式: delta_t_pp = (2 * gamma * gs * R) / (omega * c^2)
    return (2 * gamma * gs * R) / (omega * c**2) * 1e9

# --- 数据准备 ---
r_axis = np.linspace(12000, 52000, 1000)
tsci_curve = [calculate_tsci_pp(r) for r in r_axis]

# 关键轨道点
geo_r, meo_r = 42164, 26560
geo_val = calculate_tsci_pp(geo_r)
meo_val = calculate_tsci_pp(meo_r)

# --- 绘图 ---
plt.figure(figsize=(10, 7))

# 1. 绘制理论曲线 (蓝色实线)
plt.plot(r_axis, tsci_curve, 'b-', lw=2.5, label=r'$\Omega$-TSCI Prediction ($\propto R^{2.5}$)')

# 2. 绘制观测数据区间 (阴影部分)
# MEO 观测区间 (10-15 ns)
plt.axvspan(25500, 27500, ymin=10/60, ymax=15/60, color='orange', alpha=0.3, label='MEO Observed Range')
# GEO/IGSO 观测区间 (30-40 ns)
plt.axvspan(41164, 43164, ymin=30/60, ymax=40/60, color='red', alpha=0.2, label='GEO/IGSO Observed Range')

# 3. 标注理论预测点
plt.scatter([geo_r, meo_r], [geo_val, meo_val], color='navy', zorder=5)

# 标注数值标签
plt.annotate(f'GEO/IGSO: {geo_val:.2f} ns', xy=(geo_r, geo_val), xytext=(geo_r-13000, geo_val+8),
             arrowprops=dict(arrowstyle='->', color='navy'), fontsize=10)
plt.annotate(f'MEO: {meo_val:.2f} ns', xy=(meo_r, meo_val), xytext=(meo_r-8000, meo_val+12),
             arrowprops=dict(arrowstyle='->', color='navy'), fontsize=10)

# 4. 图表细节美化
plt.title('Validation of $\Omega$-TSCI Clock Anomaly Model', fontsize=14)
plt.xlabel('Orbital Radius $R$ (km)', fontsize=12)
plt.ylabel('Peak-to-Peak Anomaly $\Delta t_{pp}$ (ns)', fontsize=12)
plt.grid(True, which='both', linestyle=':', alpha=0.5)
plt.xlim(12000, 52000)
plt.ylim(0, 60)
plt.legend(loc='upper left', frameon=True)

plt.tight_layout()
plt.show()
