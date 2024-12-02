import re, math
from pathlib import Path

fname = Path(__file__).absolute().parents[1] / 'inputs' / Path(__file__).name[3:5]
with open(fname.with_suffix(".txt"), "r") as f:
    cards = list(map(lambda x: list(map(lambda y: set(map(lambda z: int(z), y.split())), filter(None, re.split(r"\w+\s+\d+:([0-9|\s]+)\|([0-9|\s]+)", x)))), f.read().splitlines()))

s1 = 0
for card in cards:
    s1 += math.floor(2**(len(card[0] & card[1])-1))

print(f"Part1: {s1}")