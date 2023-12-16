import re
from pathlib import Path

fname = Path(__file__).absolute().parents[1] / 'inputs' / Path(__file__).name[3:5]
with open(fname.with_suffix(".txt"), "r") as f:
    data = f.readline().rstrip().split(',')

def myhash(s):
    ret = 0
    for c in s:
        ret = (((ord(c)+ret)*17) % 256)
    return ret

print(f"Part1: {sum(myhash(e) for e in data)}")

####################### Part 2 #######################

hmap = [[] for _ in range(256)]

for e in data:
    label, lens = re.split(r"=|-", e)
    box = myhash(label)
    if lens:
        found = False
        for l in hmap[box]:
            if l[0] == label:
                l[1], found = int(lens), True 
        hmap[box].append([label, int(lens)]) if not found else None
    else: 
        hmap[box] = list(filter(lambda x: x[0] != label, hmap[box]))

# add up focusing powers
s = 0
for i,e in enumerate(hmap):
    s += sum([(1+i)*(1+j)*ee[1] for j,ee in enumerate(e)])

print(f"Part2: {s}")