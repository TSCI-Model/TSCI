import sys
import os
import numpy as np
import matplotlib.pyplot as plt

# [中] 将根目录添加到路径
# [En] Add root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from simulation.params import a0_pred, G
except ImportError:
    print("错误：无法导入参数中心。")
    sys.exit(1)

def plot_fig4_rotation_curves(M_solar=1e11):
    """
    [中] 复现 Fig 4: 基于预测 a0 的星系转动曲线
    [En] Reproduce Fig 4: Rotation curves based on predicted a0
    """
    # 建立输出目录
    output_dir = "observations"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 物理设置
    M = M_solar * 1.989e30  # 转换为千克
    r_kpc = np.linspace(0.5, 40, 100)
    r_meters = r_kpc * 3.08567758e19

    # 1. 牛顿引力速度 (Newtonian velocity)
    v_newton = np.sqrt(G * M / r_meters)
    
    # 2. Ω-TSCI 修正速度 (Modified velocity using a0_pred)
    # 基于 MOND 极限形式: v^4 = G * M * a0
    v_tsci_limit = np.power(G * M * a0_pred, 0.25)
    
    # 3. 全量速度曲线 (Combined profile)
    v_total = np.sqrt(v_newton**2 * 0.5 + np.sqrt((v_newton**4)/4 + (v_newton**2 * a0_pred * r_meters))) # 采用标准插值函数形式
    # 简化显示逻辑：使用预测的 a0 平坦值
    v_final = np.sqrt(v_newton**2 + v_tsci_limit**2) 

    # 绘图
    plt.figure(figsize=(9, 5))
    plt.plot(r_kpc, v_newton/1000, 'k--', label='Newtonian (Baryons Only)')
    plt.plot(r_kpc, v_final/1000, 'r-', linewidth=2, label=f'Ω-TSCI Prediction ($a_0={a0_pred:.2e}$)')
    plt.axhline(y=v_tsci_limit/1000, color='blue', linestyle=':', alpha=0.5, label='Flat limit')

    plt.title(f"Fig 4: Galaxy Rotation Curve (Mass=$10^{{{int(np.log10(M_solar))}}} M_\\odot$)")
    plt.xlabel("Radius (kpc)")
    plt.ylabel("Circular Velocity (km/s)")
    plt.legend()
    plt.grid(True, alpha=0.2)

    save_path = os.path.join(output_dir, "fig4_rotation_curve.png")
    plt.savefig(save_path)
    print(f"图表已成功保存至: {save_path}")

if __name__ == "__main__":
    plot_fig4_rotation_curves()
