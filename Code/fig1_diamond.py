import sys
import os
import numpy as np
import matplotlib.pyplot as plt

# 自动处理路径以调用 params
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
try:
    from simulation.params import gamma
except:
    gamma = 0.4977

def plot_diamond():
    fig, ax = plt.subplots(figsize=(6, 6))
    # 绘制钻石边界
    ax.plot([0, 1, 0, -1, 0], [1, 0, -1, 0, 1], 'k-', lw=2)
    # 模拟内部泊松洒点
    points = np.random.uniform(-1, 1, (150, 2))
    valid_points = points[np.abs(points[:,0]) + np.abs(points[:,1]) <= 1]
    ax.scatter(valid_points[:,0], valid_points[:,1], s=10, alpha=0.5, c='blue')
    
    ax.set_title("Fig 1: Causal Diamond Geometry")
    ax.set_aspect('equal')
    ax.axis('off')
    
    os.makedirs("visualizations", exist_ok=True)
    plt.savefig("visualizations/fig1_diamond.png")
    print("Fig 1 saved to visualizations/fig1_diamond.png")

if __name__ == "__main__":
    plot_diamond()
