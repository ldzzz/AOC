import sys
from pathlib import Path

fname = Path(__file__).absolute().parents[1] / 'inputs' / Path(__file__).name[3:5]
with open(fname.with_suffix(".txt"), "r") as f:
    data = list(map(lambda y: list(map(int, y.split())) ,map(lambda x: x.split(":")[1], f.read().split("\n\n"))))

lowest = sys.maxsize

for seed in data[0]:
    res = seed
    for a in data[1:]:
        for i in range(0, len(a), 3):
            diff = abs(a[i+1] - res)
            if res >= a[i+1] and diff < a[i+2]:
                res = diff + a[i]
                break
    lowest = res if res < lowest else lowest

print(f"Part1: {lowest}")

####################### Part 2 #######################

ranges = []
for j in range(0, len(data[0]), 2):
    to_check = [range(data[0][j], data[0][j]+data[0][j+1])]
    for a in data[1:]:
        new_ranges = []
        while to_check:
            r = to_check.pop()
            matched = False
            for i in range(0, len(a), 3):
                srcr = range(a[i+1], a[i+1]+a[i+2])
                overlapr = range(max(r.start, srcr.start), min(r.stop, srcr.stop))
                destr = range(a[i] + overlapr.start - srcr.start, a[i] + overlapr.stop - a[i+1])
                if overlapr:
                    matched = True
                    new_ranges.append(destr)
                    left = range(min(r.start, overlapr.stop), min(r.stop, overlapr.start)) # left of overlap range
                    right = range(max(r.start, overlapr.stop), max(r.stop, overlapr.start)) # right of overlap range
                    if len(left):
                        to_check.append(left)
                    if len(right):
                        to_check.append(right)
            if not matched:
                new_ranges.append(r)
        to_check = new_ranges
    ranges += to_check


print(f"Part2: {min(r.start for r in ranges)}")

