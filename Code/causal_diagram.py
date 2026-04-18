import matplotlib.pyplot as plt
import networkx as nx

# 创建有向图
G = nx.DiGraph()

# 添加节点：x (中心), 直接前驱 y1,y2,y3, 更深层节点 z1,z2,z3
nodes = ['x', 'y1', 'y2', 'y3', 'z1', 'z2', 'z3']
G.add_nodes_from(nodes)

# 添加边：构建因果层次
# y1,y2,y3 是 x 的直接前驱 (最小邻域)
edges = [('y1', 'x'), ('y2', 'x'), ('y3', 'x'),
         ('z1', 'y1'), ('z2', 'y2'), ('z3', 'y3'),
         # 冗余路径：z2 到 x 的额外路径（通过 y3？或其他），这里画一条虚线冗余
         ('z2', 'y3')]
G.add_edges_from(edges)

# 定义节点位置（手动布局，使图清晰）
pos = {
    'x':  (0, 0),
    'y1': (-1, 1),
    'y2': (0, 1.2),
    'y3': (1, 1),
    'z1': (-2, 2),
    'z2': (0, 2.5),
    'z3': (2, 2)
}

# 绘图
plt.figure(figsize=(6, 5), dpi=300)
ax = plt.gca()

# 绘制普通边（黑色实线）
nx.draw_networkx_edges(G, pos, edgelist=[e for e in edges if e != ('z2', 'y3')],
                       edge_color='black', width=1.5, arrows=True, arrowsize=15,
                       connectionstyle="arc3,rad=0.1")

# 绘制冗余路径（红色虚线）
nx.draw_networkx_edges(G, pos, edgelist=[('z2', 'y3')],
                       edge_color='red', width=2, style='dashed', arrows=True, arrowsize=15,
                       connectionstyle="arc3,rad=0.3")

# 绘制节点
nx.draw_networkx_nodes(G, pos, node_size=800, node_color='lightblue', edgecolors='black')
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

# 添加标注：最小邻域 ∂P(x) 的说明
# 用椭圆圈出 y1,y2,y3
from matplotlib.patches import Ellipse
ell = Ellipse(xy=(0, 1.2), width=2.2, height=1.0, edgecolor='blue', facecolor='none', linestyle='--', linewidth=1.5)
ax.add_patch(ell)
ax.text(0, 1.6, r'$\partial\mathcal{P}(x)$', color='blue', fontsize=12, ha='center')

# 添加过去锥标注
ax.annotate(r'$\mathcal{P}(x)$', xy=(-2.5, 2.2), xytext=(-3, 2.8),
            arrowprops=dict(arrowstyle='->', color='gray'), fontsize=12)

# 添加节点 x 标注
ax.text(0, -0.3, r'$x$', fontsize=14, fontweight='bold', ha='center')

# 添加冗余路径的图例
ax.plot([], [], 'r--', label='Redundant path')
ax.plot([], [], 'k-', label='Causal link')
ax.legend(loc='upper left', fontsize=9)

plt.title('Causal structure: past cone $\mathcal{P}(x)$ and minimal neighbourhood $\partial\mathcal{P}(x)$', fontsize=11)
plt.axis('off')
plt.tight_layout()
plt.savefig('causal_diagram.png', dpi=300, bbox_inches='tight')
plt.show()
