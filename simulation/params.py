import numpy as np

# [中] Omega-TSCI 统一参数管理
# [En] Unified Parameter Management for Omega-TSCI

# 1. 核心标度指数 (Core Scaling Index)
# 对应论文 Fig 3 的 WLS 拟合结果
gamma = 0.4977 

# 2. 宇宙学常数 (Cosmological Constants)
H0_km_s_mpc = 67.4  # 哈勃常数 (Hubble Constant)
c = 299792458.0      # 光速 m/s (Speed of Light)
G = 6.67430e-11      # 万有引力常数 (Gravitational Constant)

# 3. 几何修正因子 (Geometric Correction Factors)
# 对应附录 C 中的 FLRW 曲率修正
fc = 1.111 

# 4. 衍生常数计算 (Derived Constants)
# 转换为国际单位制 s^-1
H0_si = H0_km_s_mpc * 1000 / 3.08567758e22 

# 拓扑因子 xi
xi = 1 / (2 * np.pi * np.sqrt(2))

# 预测的 MOND a0
a0_pred = (c * H0_si * xi / np.sqrt(gamma)) * fc

# 预测的张量谱指数 nT
nT_pred = 1 - 3 * gamma
