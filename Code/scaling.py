import numpy as np
import matplotlib.pyplot as plt
import os
import sys

# 路径对齐
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def generate_causal_diamond():
    N = 600
    u = np.random.uniform(0, 1, N)
    v = np.random.uniform(0, 1, N)
    t = (u + v) / 2
    x = (v - u) / 2
    
    boundary_x = [0, 0.5, 0, -0.5, 0]
    boundary_t = [0, 0.5, 1, 0.5, 0]
    
    plt.rcParams.update({"font.family": "serif", "mathtext.fontset": "cm", "font.size": 11})
    plt.figure(figsize=(7, 7), dpi=300)
    plt.scatter(x, t, s=10, c='black', alpha=0.6, label=r'Nodes ($\mathcal{N}=600$)')
    plt.plot(boundary_x, boundary_t, color='#d62728', lw=2)
    plt.fill(boundary_x, boundary_t, color='#1f77b4', alpha=0.1)
    
    plt.xlabel(r'$x$'); plt.ylabel(r'$t$')
    plt.gca().set_aspect('equal')
    
    # 核心修正：确保文件夹存在
    os.makedirs("visualizations", exist_ok=True)
    plt.savefig('visualizations/fig1_diamond.png', bbox_inches='tight')
    print("Successfully saved: visualizations/fig1_diamond.png")

if __name__ == "__main__":
    generate_causal_diamond()
