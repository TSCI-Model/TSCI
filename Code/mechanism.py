import numpy as np
import matplotlib.pyplot as plt

def draw_mechanism_v2():
    # 使用更具学术感的样式
    plt.style.use('seaborn-v0_8-paper')
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # 1. 绘制地球 (中心主天体)
    earth = plt.Circle((0, 0), 0.15, color='royalblue', zorder=5, label='Earth')
    ax.add_artist(earth)
    
    # 2. 绘制卫星轨道 (虚线)
    orbit = plt.Circle((0, 0), 1.0, color='gray', fill=False, linestyle='--', zorder=3)
    ax.add_artist(orbit)
    
    # 3. 绘制背景场：Warp Factor Gradient (nabla phi)
    # 替代了原来的 Solar Gravity Gradient，直接关联论文的核心微扰项
    x_grads = np.linspace(-1.5, 1.5, 12)
    y_grads = np.linspace(-1.5, 1.5, 12)
    X, Y = np.meshgrid(x_grads, y_grads)
    ax.quiver(X, Y, np.ones_like(X), np.zeros_like(Y), 
              color='darkorange', alpha=0.3, width=0.005,
              label=r'Warp Factor Gradient $\nabla\phi$')

    # 4. 标注关键物理位置：正午 (Noon) 和 午夜 (Midnight)
    # 正午：向着太阳引力源方向
    ax.scatter([1.0], [0], color='red', s=100, zorder=6, label='Noon (Max Anomaly)')
    # 午夜：背离太阳引力源方向
    ax.scatter([-1.0], [0], color='blue', s=100, zorder=6, label='Midnight (Min Anomaly)')
    
    # 5. 绘制任意轨道位置的动力学矢量
    theta = np.pi / 4  # 取 45 度角位置作为图解
    sat_x, sat_y = np.cos(theta), np.sin(theta)
    ax.scatter([sat_x], [sat_y], color='black', s=60, zorder=6) # 卫星当前位置
    
    # 速度矢量 v (沿切线方向)
    ax.quiver(sat_x, sat_y, -np.sin(theta), np.cos(theta), 
              color='green', scale=4, scale_units='xy', angles='xy', width=0.008,
              zorder=7, label=r'Velocity $\vec{v}$')
              
    # 局部太阳引力加速度矢量 g_S (水平向右)
    ax.quiver(sat_x, sat_y, 0.4, 0, 
              color='crimson', scale=1, scale_units='xy', angles='xy', width=0.008,
              zorder=7, label=r'Solar Gravitational Accel. $\vec{g}_S$')

    # 6. 图表装饰与布局设定
    ax.set_xlim(-1.6, 1.6)
    ax.set_ylim(-1.6, 1.6)
    ax.set_aspect('equal') # 确保轨道是正圆
    
    # 添加标题和坐标轴标签 (PRD风格通常偏好清晰的LaTeX渲染)
    ax.set_title(r'Physical Mechanism: Satellite in Non-factorizable Geometry', fontsize=14, pad=15)
    ax.set_xlabel('Orbital Plane X-axis (Towards Sun)', fontsize=12)
    ax.set_ylabel('Orbital Plane Y-axis', fontsize=12)
    
    # 将图例放在外面或合适的位置避免遮挡
    ax.legend(loc='upper right', bbox_to_anchor=(1.35, 1.0), fontsize=11, framealpha=1)
    
    # 移除多余的网格边框以保持学术图表的干净
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(True, linestyle=':', alpha=0.6)
    
    plt.tight_layout()
    plt.show()

# 执行绘图
draw_mechanism_v2()
