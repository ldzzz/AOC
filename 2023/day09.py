import numpy as np
from pathlib import Path

fname = Path(__file__).absolute().parents[1] / 'inputs' / Path(__file__).name[3:5]
with open(fname.with_suffix(".txt"), "r") as f:
    histories = list(map(lambda x: np.array(list(map(int, x.split()))), f.read().splitlines()))

s = 0
for history in histories:
    a = history
    while np.any(a):
        s, a = s + a[-1], np.diff(a)

print(f"Part1: {s}")

####################### Part 2 #######################

s = 0
for history in histories:
    a, v = history, [a[0]]
    while np.any(a):
        v.append(a[0])
        a = np.diff(a)
    ss = 0
    for i in range(len(v)-1, 0, -1):
        ss = v[i] - ss
    s += ss

print(f"Part2: {s}")