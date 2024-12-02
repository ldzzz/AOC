from pathlib import Path
import re

fname = Path(__file__).absolute().parents[1] / 'inputs' / Path(__file__).name[3:5]
with open(fname.with_suffix(".txt"), "r") as f:
    data = map(lambda x: x.split(' -> '), f.read().splitlines())

wirings = []
for a,b in data:
    out = b.split(", ")
    if a == "broadcaster":
        tmp = {"name": a, "in": ["button"], "out": out, "op": None, "mem": [], "status": 0}
    else:
        r = list(filter(None, re.split(r"(%|&)", a)))
        ins = [x["name"] for x in wirings if r[1] in x["out"]]
        tmp["op"]   = {"name": r[1], "in": ins, "out": out, "op": r[0], "mem": [], "status": 0}
    wirings.append(tmp)

for e in wirings:
    print(e)

############################ Part2 ############################