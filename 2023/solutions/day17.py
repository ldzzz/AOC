from pathlib import Path
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

fname = Path(__file__).absolute().parents[1] / 'inputs' / Path(__file__).name[3:5]
with open(fname.with_suffix(".txt"), "r") as f:
    grid = list(map(lambda x: list(map(int, list(x))), f.read().splitlines()))


A = np.array(grid)
G = nx.from_numpy_array(A)
 

G = nx.grid_2d_graph(3,3)  # 13x13 grid
# This example needs Graphviz and PyGraphviz

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if j+1 < len(grid[i]):
            G.add_edge((i,j), (i, j+1), weight=grid[i][j+1])
        if j-1 >= 0:
            G.add_edge((i,j), (i, j-1), weight=grid[i][j-1])
        if i+1 < len(grid):
            G.add_edge((i,j), (i+1, j), weight=grid[i+1][j])
        if i-1 >= 0:
            G.add_edge((i,j), (i-1, j), weight=grid[i-1][j])


print(nx.dijkstra_path(G, (0,0), (12,12), weight="weight"))
pos = nx.nx_agraph.graphviz_layout(G)
nx.draw_networkx(G, pos)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.show()




