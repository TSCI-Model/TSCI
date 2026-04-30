import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 1. 设定模拟参数 (基于论文描述)
N_values = np.logspace(np.log10(2000), np.log10(200000), 15)  # N 范围 2k 到 200k
gamma_true = 0.4933  # 论文测得的缩放指数
A = 0.1  # 比例系数 (示意值)

# 2. 生成模拟观测数据 (模拟 100 次实现的均方根波动[cite: 7])
# 加上符合泊松分布特征的随机噪声
np.random.seed(42)
dS_BD = A * (N_values**gamma_true) * (1 + 0.02 * np.random.normal(size=len(N_values)))
errors = 0.02 * dS_BD  # 模拟标准差

# 3. 定义拟合函数: y = a * x^gamma
def power_law(N, a, g):
    return a * (N**g)

# 4. 执行加权最小二乘法拟合[cite: 7]
popt, pcov = curve_fit(power_law, N_values, dS_BD, p0=[0.1, 0.5], sigma=errors)
a_fit, g_fit = popt
g_error = np.sqrt(np.diag(pcov))[1]

# 5. 绘图 (还原论文 Figure 1 风格[cite: 7])
plt.figure(figsize=(8, 6))
plt.errorbar(N_values, dS_BD, yerr=errors, fmt='o', color='black', 
             ecolor='gray', capsize=3, label='Numerical Data (100 realizations)')
plt.plot(N_values, power_law(N_values, *popt), 'r-', 
         label=rf'Fit: $\gamma = {g_fit:.4f} \pm {g_error:.4f}$')

# 设置对数坐标轴[cite: 7]
plt.xscale('log')
plt.yscale('log')

# 标签与格式
plt.xlabel(r'Causal Set Size $\mathcal{N}$', fontsize=12)
plt.ylabel(r'RMS Fluctuation $\delta\mathcal{S}_{\rm BD}$', fontsize=12)
plt.title('Scaling of Benincasa-Dowker Action Fluctuations')
plt.grid(True, which="both", ls="-", alpha=0.2)
plt.legend()

print(f"拟合得到的 Gamma 指数: {g_fit:.4f}")
print(f"拟合偏差: {g_error:.4f}")

plt.show()
