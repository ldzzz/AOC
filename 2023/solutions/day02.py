import re
from pathlib import Path

fname = Path(__file__).absolute().parents[1] / 'inputs' / Path(__file__).name[3:5]
with open(fname.with_suffix(".txt"), "r") as f:
    lines = list(map(lambda x: x.split(": ")[1].split("; "), f.read().splitlines()))

s1, s2 = 0, 0
for i in range(0, len(lines)):
    tmp = {"red": [], "green": [], "blue": []}
    for e in lines[i]:
        for aa in re.findall(r"(\d+)\s(red|green|blue)", e):
            tmp[aa[1]].append(int(aa[0]))
    lines[i] = tmp

for i in range(0, len(lines)):
    r,g,b = max(lines[i]["red"]), max(lines[i]["green"]), max(lines[i]["blue"])
    s1 = s1+i+1 if r <= 12 and g <= 13 and b <= 14 else s1
    s2+=r*g*b

print(f"Part1: {s1}\nPart2: {s2}")