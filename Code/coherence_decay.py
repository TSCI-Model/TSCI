# -*- coding: utf-8 -*-
"""Ω-TSCI 退相干率计算与绘图（带箭头标注，正确版本）"""

import numpy as np
import matplotlib.pyplot as plt

# 常数
hbar = 1.0545718e-34
tP = 5.391247e-44
gamma = 0.4933
gS = 0.00593
dx = 1e-6          # 1 μm
m_macro = 1e-2     # 10 g

def decoherence_rate(m, theta_deg):
    if abs(theta_deg - 90) < 1e-9:
        return 0.0
    theta_rad = np.deg2rad(theta_deg)
    cos_theta = np.cos(theta_rad)
    return (m**2 * gamma**2 * tP * (gS * dx)**2 * cos_theta**2) / (2 * hbar**2)

Gamma = decoherence_rate(m_macro, 0)
print(f"Γ = {Gamma:.2e} s⁻¹")
print(f"1/e time = {1/Gamma:.2e} s")
print(f"Coherence at 1 ms = {np.exp(-Gamma*1e-3):.3f}")

t = np.logspace(-6, -2, 500)
coh = np.exp(-Gamma * t)

plt.figure(figsize=(8,6))
plt.semilogx(t, coh, 'r-', linewidth=2, label='Macroscopic (10 g), θ = 0°')
plt.semilogx(t, np.ones_like(t), 'b--', linewidth=2, label='Macroscopic (10 g), θ = 90°')
plt.semilogx(t, np.ones_like(t), 'g-.', linewidth=2, label='Electron, θ = 0°')

# 标注 1/e 点
t_one_e = 1 / Gamma
plt.plot(t_one_e, np.exp(-1), 'ro', markersize=8)
plt.annotate(r'$t = 1/\Gamma = 0.48$ ms', xy=(t_one_e, np.exp(-1)),
             xytext=(t_one_e*2, 0.5), arrowprops=dict(arrowstyle='->', color='red'))

# 标注 1 ms 点
t_1ms = 1e-3
coh_1ms = np.exp(-Gamma * t_1ms)
plt.plot(t_1ms, coh_1ms, 'bo', markersize=8)
plt.annotate(r'$t = 1$ ms, coh = 0.126', xy=(t_1ms, coh_1ms),
             xytext=(t_1ms*0.5, 0.3), arrowprops=dict(arrowstyle='->', color='blue'))

plt.xlabel('Time (s)')
plt.ylabel(r'Coherence $|\rho_{12}(t)/\rho_{12}(0)|$')
plt.title('Decoherence due to Ω-TSCI geometric noise')
plt.ylim(-0.05, 1.05)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('coherence_decay_annotated.png', dpi=300)
plt.show()
