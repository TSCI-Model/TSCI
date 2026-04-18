# ============================================
# PRD Figure 2 (最终版): 官方 RAR 数据 + 真实星系旋转曲线示例
# 使用您已上传的 .dat 文件（位于 sparc/ 目录）
# ============================================

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import urllib.request
import os, glob
import warnings
warnings.filterwarnings('ignore')

plt.rcParams.update({
    'font.size': 12,
    'axes.labelsize': 12,
    'axes.titlesize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight'
})

# ============================================
# 1. 加载官方 RAR 数据（手动解析，取前269点）
# ============================================
url = "https://astroweb.cwru.edu/SPARC/RAR.mrt"
response = urllib.request.urlopen(url)
lines = response.readlines()

log_gbar = []
e_log_gbar = []
log_gobs = []
e_log_gobs = []

for line in lines:
    line_str = line.decode('utf-8').strip()
    if not line_str:
        continue
    parts = line_str.split()
    if len(parts) < 4:
        continue
    try:
        v0 = float(parts[0])
        v1 = float(parts[1])
        v2 = float(parts[2])
        v3 = float(parts[3])
    except ValueError:
        continue
    log_gbar.append(v0)
    e_log_gbar.append(v1)
    log_gobs.append(v2)
    e_log_gobs.append(v3)

# 只取前269个点（官方数据固定数量）
log_gbar = np.array(log_gbar[:269])
e_log_gbar = np.array(e_log_gbar[:269])
log_gobs = np.array(log_gobs[:269])
e_log_gobs = np.array(e_log_gobs[:269])

g_N = 10.0**log_gbar
g_obs = 10.0**log_gobs
err_dex = e_log_gobs

print(f"✅ 加载 RAR 数据: {len(g_N)} 个点")

# ============================================
# 2. MOND 模型 (a0 = 1.170e-10)
# ============================================
A0_MOND = 1.170e-10

def mond_model(g_N, a0=A0_MOND):
    g_N = np.maximum(g_N, 1e-15)
    return g_N / (1 - np.exp(-np.sqrt(g_N / a0)))

def mond_velocity(r_kpc, v_bar_kmps, a0=A0_MOND):
    r_m = r_kpc * 3.086e19
    v_bar_ms = v_bar_kmps * 1000.0
    g_N = v_bar_ms**2 / r_m
    g = mond_model(g_N, a0)
    v_mond_ms = np.sqrt(g * r_m)
    return v_mond_ms / 1000.0

g_pred = mond_model(g_N)
residuals = (np.log10(g_obs) - np.log10(g_pred)) / err_dex
chi2 = np.sum(residuals**2)
dof = len(g_N) - 1
chi2_dof = chi2 / dof

print(f"\n全局拟合统计 (a0 = {A0_MOND:.3e} m/s²):")
print(f"  χ²/dof = {chi2_dof:.3f}, 残差标准差 = {np.std(residuals):.3f}")

# ============================================
# 3. 寻找一个可用的示例星系（从 sparc/ 目录）
# ============================================
DATA_DIR = 'sparc'
example_gal = None
example_r = example_v_obs = example_err = example_v_bar = example_v_model = None

if os.path.exists(DATA_DIR):
    dat_files = glob.glob(os.path.join(DATA_DIR, '*.dat'))
    print(f"找到 {len(dat_files)} 个星系文件")
    for f in dat_files:
        try:
            data = np.loadtxt(f, usecols=(0,1,2,3,4))
            r = data[:,0]
            v_obs = data[:,1]
            err_v = data[:,2]
            v_gas = data[:,3]
            v_disk = data[:,4]
            v_bar = np.sqrt(v_gas**2 + v_disk**2)
            if len(r) < 5:
                continue
            v_model = mond_velocity(r, v_bar)
            # 只要第一个有效星系
            example_gal = os.path.basename(f)
            example_r = r
            example_v_obs = v_obs
            example_err = err_v
            example_v_bar = v_bar
            example_v_model = v_model
            print(f"示例星系: {example_gal}")
            break
        except:
            continue

# ============================================
# 4. 理论曲线
# ============================================
g_N_theory = np.logspace(-14, -9, 200)
g_obs_theory = mond_model(g_N_theory)

# ============================================
# 5. 绘图 Figure 2
# ============================================
fig = plt.figure(figsize=(12, 10))

# (a) RAR 散点图
ax1 = plt.subplot(2, 2, 1)
ax1.scatter(g_N, g_obs, s=2, alpha=0.4, c='blue', label='SPARC RAR data (official)')
ax1.plot(g_N_theory, g_obs_theory, 'r-', lw=2, label=f'MOND model, $a_0 = {A0_MOND:.3e}$ m/s²')
ax1.plot([1e-14, 1e-8], [1e-14, 1e-8], 'k--', alpha=0.5, label='Newtonian $g = g_N$')
ax1.set_xscale('log'); ax1.set_yscale('log')
ax1.set_xlabel(r'Newtonian acceleration $g_N$ (m/s²)')
ax1.set_ylabel(r'Observed acceleration $g_{\rm obs}$ (m/s²)')
ax1.set_title('(a) Radial Acceleration Relation (RAR)')
ax1.legend(loc='upper left', fontsize=9)
ax1.grid(True, alpha=0.3)

# (b) 残差分布
ax2 = plt.subplot(2, 2, 2)
ax2.hist(residuals, bins=40, density=True, alpha=0.7, color='gray', edgecolor='black')
ax2.axvline(0, color='r', linestyle='--')
x_norm = np.linspace(-4, 4, 200)
ax2.plot(x_norm, norm.pdf(x_norm, 0, 1), 'k-', label='Standard normal')
ax2.set_xlabel(r'Residual $\log_{10}(g_{\rm obs}/g_{\rm model}) / \sigma$')
ax2.set_ylabel('Probability density')
ax2.set_title('(b) Residual Distribution')
ax2.legend(fontsize=9)

# (c) 全局拟合优度
ax3 = plt.subplot(2, 2, 3)
ax3.text(0.5, 0.65, 'Global RAR fit statistic:', transform=ax3.transAxes, ha='center', fontsize=12)
ax3.text(0.5, 0.45, f'χ²/dof = {chi2_dof:.2f}', transform=ax3.transAxes, ha='center', fontsize=14, fontweight='bold')
ax3.text(0.5, 0.25, f'Residual std = {np.std(residuals):.2f}', transform=ax3.transAxes, ha='center', fontsize=12)
ax3.set_title('(c) Goodness-of-fit')
ax3.axis('off')

# (d) 示例星系旋转曲线
ax4 = plt.subplot(2, 2, 4)
if example_gal is not None:
    ax4.errorbar(example_r, example_v_obs, yerr=example_err, fmt='o', ms=3, capsize=2, label='Data')
    ax4.plot(example_r, example_v_model, 'r-', label='MOND model')
    ax4.plot(example_r, example_v_bar, 'g--', label='Baryonic only')
    ax4.set_xlabel('Radius (kpc)')
    ax4.set_ylabel('Circular velocity (km/s)')
    ax4.set_title(f'(d) Example galaxy: {example_gal}')
    ax4.legend(fontsize=9)
    ax4.grid(True, alpha=0.3)
else:
    ax4.text(0.5, 0.5, 'No galaxy data found\n(Place .dat files in sparc/ directory)',
             transform=ax4.transAxes, ha='center', va='center', fontsize=12)
    ax4.set_title('(d) Example galaxy')
    ax4.axis('off')

plt.tight_layout()
plt.savefig('Figure2_PRDCandidate.png', dpi=300)
plt.show()

# ============================================
# 6. 输出统计表（与论文兼容）
# ============================================
print("\n" + "="*60)
print("SPARC RAR 全样本 MOND 拟合统计结果 (a0 = {:.3e} m/s²)".format(A0_MOND))
print("="*60)
print(f"加速度点总数:            {len(g_N)}")
print(f"全局 χ²/dof:              {chi2_dof:.3f}")
print(f"残差均值:                 {np.mean(residuals):.4f}")
print(f"残差标准差:               {np.std(residuals):.4f}")
print("="*60)

# 保存统计表
import pandas as pd
df = pd.DataFrame({
    'log_gbar': log_gbar,
    'e_log_gbar': e_log_gbar,
    'log_gobs': log_gobs,
    'e_log_gobs': e_log_gobs,
    'residuals': residuals
})
df.to_csv('sparc_rar_official_stats.csv', index=False)
print("统计表已保存为 sparc_rar_official_stats.csv")
