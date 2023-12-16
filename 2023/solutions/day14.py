import sys, re
from operator import itemgetter

with open(f"../inputs/{sys.argv[1]}.txt", "r") as f:
    data = f.read().splitlines()

cols = [''.join(list(map(itemgetter(i), data))) for i in range(len(data[0]))]

def shift_north(col, colen, indexes, s):
    if len(indexes) < 2:
        return s
    start = indexes.pop(0)+1
    end = indexes[0]
    a = col[start:end].count('O')
    return shift_north(col, colen, indexes, s+sum([colen]*a) - sum(range(start, a+start)))

s = 0
for col in cols:
    indexes = [x.start() for x in re.finditer('#', col)]
    indexes = [-1]+indexes + [len(col)]
    s += shift_north(col, len(col), indexes, 0)

print(f"Part1: {s}")
