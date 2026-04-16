import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import toeplitz

# 模拟因果集协方差矩阵
# Simulate the covariance matrix for a causal set

# 对角元为1，非对角元随"间隔距离"指数衰减
# Diagonal entries are 1, off-diagonals decay exponentially with "interval distance"
np.random.seed(42)
N = 200  # 矩阵维度 / Matrix dimension
rho = 0.85  # 相邻间隔的相关性 / Correlation between adjacent intervals
decay = np.array([rho**k for k in range(N)])
cov_matrix = toeplitz(decay)

# 添加微小噪声使其看起来更真实
# Add small noise to make it look more realistic
noise = np.random.normal(0, 0.05, (N, N))
cov_matrix += noise

# 保证对称正定
# Ensure symmetric positive definite
cov_matrix = (cov_matrix + cov_matrix.T) / 2

# 归一化（使对角为1）
# Normalize (set diagonal to 1)
d = np.sqrt(np.diag(cov_matrix))
cov_norm = cov_matrix / np.outer(d, d)

# 绘图
# Plotting
fig, ax = plt.subplots(figsize=(8, 6))
im = ax.imshow(cov_norm, cmap='RdBu_r', vmin=-0.5, vmax=1.0, aspect='auto')
ax.set_title("Normalized Covariance Matrix of $N_{pq}$", fontsize=14)
ax.set_xlabel("Interval index $j$", fontsize=12)
ax.set_ylabel("Interval index $i$", fontsize=12)
cbar = plt.colorbar(im, ax=ax)
cbar.set_label("Correlation coefficient", fontsize=12)
ax.plot([0, N-1], [0, N-1], 'w--', linewidth=0.5, alpha=0.5)

plt.tight_layout()
plt.savefig("cov_matrix.png", dpi=600)
plt.show()

# 图形已保存为 cov_matrix.png
print("Figure saved as cov_matrix.png")
