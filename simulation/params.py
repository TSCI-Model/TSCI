import numpy as np

# [中] Omega-TSCI 统一参数管理中心
# [En] Unified Parameter Management Center for Omega-TSCI

# --- 核心物理输入 (Core Physical Inputs) ---
gamma = 0.4933        # 标度指数 (Scaling Index)
H0_km_s_mpc = 67.4    # 哈勃常数 (Hubble Constant)
fc = 1.111            # FLRW 几何修正因子 (Curvature Correction)

# --- 物理常数 (Physical Constants) ---
c = 299792458.0       # 光速 (m/s)
G = 6.67430e-11       # 万有引力常数 (SI)

# --- 派生常数 (Derived Constants) ---
# 转换为 s^-1 (Convert to SI units)
H0_si = H0_km_s_mpc * 1000 / 3.08567758e22 

# 拓扑因子 (Topological Factor xi)
xi = 1 / (2 * np.pi * np.sqrt(2))

# 预测的 MOND a0 (Predicted a0)
a0_pred = (c * H0_si * xi / np.sqrt(gamma)) * fc

# 预测的张量谱指数 (Predicted nT)
nT_pred = 1 - 3 * gamma

# 密度比预测 (Predicted DM/DE Ratio)
ratio_pred = gamma / (np.exp(1) / 2)
