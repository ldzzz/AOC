import sys
import math
import itertools
from pathlib import Path

fname = Path(__file__).absolute().parents[1] / 'inputs' / Path(__file__).name[3:5]
with open(fname.with_suffix(".txt"), "r") as f:
    data = list(map(lambda y: [y[0], list(map(int, y[1].split(',')))], map(lambda x: x.split() ,f.read().splitlines())))


for i in range(0, len(data)):
    data[i][0] = ((data[i][0] + "?") *5)[:-1]
    data[i][1] = list(itertools.chain.from_iterable(itertools.repeat(data[i][1], 5)))
res = 0
for e in data:
    s = list(filter(None, e[0].split('.')))
    if not len(s) <= len(e[1]):
        print(s)
        print(e[1])
    for i in range(len(s)):
        if s[i].count('#') == e[1][i]:
            continue
        else:
            a = math.comb(len(s[i]), e[1][i])
            res += a
    print('-'*50)


print(f"Part1: {res}")

itertools.combinations()

