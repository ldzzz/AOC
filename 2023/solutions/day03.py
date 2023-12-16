import re
from functools import reduce
from pathlib import Path

fname = Path(__file__).absolute().parents[1] / 'inputs' / Path(__file__).name[3:5]
with open(fname.with_suffix(".txt"), "r") as f:
    data = list(map(lambda x: list(x), f.read().splitlines()))

symbols = []

for i in range(1, len(data)-1):
    for j in range(0, len(data[0])):
        if re.search(r"[^0-9|^\.]", data[i][j]):
            tmp = []
            # check left-right
            off = 1
            while j-off > 0 and data[i][j-off].isdigit():
                off +=1
            if off > 1:
                a = re.split(r"[^0-9]", ''.join(data[i][j-off:j]))
                for e in filter(None, a):
                    tmp.append(int(e))
            off = 1
            while j+off < len(data[0]) and data[i][j+off].isdigit():
                off +=1
            if off > 1:
                a = re.split(r"[^0-9]", ''.join(data[i][j+1:j+off]))
                for e in filter(None, a):
                    tmp.append(int(e))
            # check above
            off1 = off2 = 1
            while j-off1 > 0 and data[i-1][j-off1].isdigit():
                off1 += 1    
            while j+off2 < len(data[0]) and data[i-1][j+off2].isdigit():
                off2 += 1
            a = re.split(r"[^0-9]", ''.join(data[i-1][j-off1:j+off2]))
            for e in filter(None, a):
                tmp.append(int(e))
            # check under
            off1 = off2 = 1
            while j-off1 > 0 and data[i+1][j-off1].isdigit():
                off1 += 1    
            while j+off2 < len(data[0]) and data[i+1][j+off2].isdigit():
                off2 += 1
            a = re.split(r"[^0-9]", ''.join(data[i+1][j-off1:j+off2]))
            for e in filter(None, a):
                tmp.append(int(e)) 
            if len(tmp):
                symbols.append({data[i][j]: tmp})

s1, s2 = 0, 0
for e in symbols:
    for k, v in e.items():
        s1 += sum(v)
        if k == '*' and len(v) == 2:
            s2 += reduce(lambda x,y: x*y,v)

print(f"Part1: {s1}\nPart2: {s2}")