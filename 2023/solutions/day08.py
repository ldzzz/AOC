import json
from math import lcm
from pathlib import Path

fname = Path(__file__).absolute().parents[1] / 'inputs' / Path(__file__).name[3:5]
with open(fname.with_suffix(".txt"), "r") as f:
          steps, navig = f.read().split('\n\n')

navig = json.loads('{"' + navig.replace(" = ", f'":').replace("(", '{"L":"').replace(", ", '","R":"').replace(")", '"},').replace('\n', '"')[:-1] + "}")

i, l, w = 0, len(steps), "AAA"
while w != "ZZZ":
    w, i = navig[w][steps[i % l]], i+1

print(f"Part1: {i}")

####################### Part 2 #######################

start_nodes = [x for x in navig.keys() if x.endswith('A')]

lcms = []
for e in start_nodes:
    cn, i = e, 0
    while not cn.endswith("Z"):
        cn, i = navig[cn][steps[i % len(steps)]], i+1
    lcms.append(i)
   
print(f"Part2: {lcm(*lcms)}")