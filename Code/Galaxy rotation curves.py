import matplotlib.pyplot as plt
import numpy as np

def plot_rotation_curves(M_solar=1e11):
    """
    复现 Fig 5: 星系转动曲线
    Reproduce Fig 5: Galaxy rotation curves
    """
    G = 6.674e-11
    M = M_solar * 1.989e30
    a0 = 1.16e-10 # 基于 gamma=0.4933 的预测值
    
    r_kpc = np.linspace(0.1, 30, 100)
    r_m = r_kpc * 3.086e19
    
    # 牛顿引力 (Newtonian)
    v_newton = np.sqrt(G * M / r_m)
    # Omega-TSCI 修正引力 (Modified gravity)
    v_tsci = (G * M * a0)**0.25
    # 最终速度 (Final velocity profile)
    v_final = np.sqrt(v_newton**2 + v_tsci**2)
    
    plt.plot(r_kpc, v_final/1000, 'r-', label='$\Omega$-TSCI (Predicted)')
    plt.plot(r_kpc, v_newton/1000, 'k--', label='Newtonian')
    plt.title(f"Rotation Curve for $M = 10^{{{np.log10(M_solar):.0f}}} M_\\odot$")
    plt.xlabel("Radius (kpc)"); plt.ylabel("Velocity (km/s)")
    plt.legend(); plt.grid(True)
    plt.show()

if __name__ == "__main__":
    plot_rotation_curves()
