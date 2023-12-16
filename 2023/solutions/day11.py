import numpy as np
from itertools import combinations
from pathlib import Path

fname = Path(__file__).absolute().parents[1] / 'inputs' / Path(__file__).name[3:5]
with open(fname.with_suffix(".txt"), "r") as f:
    data = np.array(list(map(lambda x: list(map(int,list(x))), f.read().replace('.', "0").replace('#', "1").splitlines())))

cols, rows = list(data.sum(axis=0)), list(data.sum(axis=1))

ceg, factor = [[], []], [1, 999999]
for galaxy in list(zip(*np.where(data == 1))):
    xoff, yoff = list(rows)[0: galaxy[0]].count(0), list(cols)[0: galaxy[1]].count(0)
    ceg[0].append((galaxy[0] + xoff*factor[0], galaxy[1] + yoff*factor[0]))
    ceg[1].append((galaxy[0] + xoff*factor[1], galaxy[1] + yoff*factor[1]))

# calculate Manhattan distance between galaxy pairs
distances = [[], []]
for gp in list(zip(list(combinations(ceg[0], 2)), list(combinations(ceg[1], 2)))):    
    distances[0].append(abs(gp[0][0][0]- gp[0][1][0]) + abs(gp[0][0][1] - gp[0][1][1]))
    distances[1].append(abs(gp[1][0][0]- gp[1][1][0]) + abs(gp[1][0][1] - gp[1][1][1]))

print(f"Part1: {sum(distances[0])}\nPart2: {sum(distances[1])}")