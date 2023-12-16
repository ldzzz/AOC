from pathlib import Path

fname = Path(__file__).absolute().parents[1] / 'inputs' / Path(__file__).name[3:5]
with open(fname.with_suffix(".txt"), "r") as f:
    data = f.read().splitlines()

# 7 different suites
suites = [[],[],[],[],[],[],[]]
def find_best(hand):
    chrs = list(set(hand))
    if '1' not in chrs:
        return hand
    hc = None
    cnt = 0
    try:
        for c in chrs:
            z = hand.count(c)
            if z > cnt and c != '1':
                cnt = z
                hc = c
        new_hand = hand.replace('1', hc)
    except Exception as e:
        return hand
    return new_hand

# sort by rank
for e in data:
   a = e.split()
   a[0] = a[0].replace('A', 'E').replace('K', 'D').replace('Q', 'C').replace('J', '1').replace('T', 'A')
   tmp = find_best(a[0])
   l = list(set(tmp))
   if len(l) == 1:
       suites[0].append(a)
   elif len(l) == 2: # either index 1 or 2
        for c in l:
            s = tmp.count(c)
            if s == 3:
                suites[2].append(a)
                break
            if s == 4:
                suites[1].append(a)
                break
   elif len(l) == 3: # either index 3 or 4
        for c in l:
            s = tmp.count(c)
            if  s == 3:
                suites[3].append(a)
                break
            if s == 2:
                suites[4].append(a)
                break
   else:
       suites[len(l)+1].append(a)

final = []
# sort inidividual ranks by strength
for e in suites:
    final += sorted(e, reverse=True)

for e in final:
    e[0] = e[0].replace('E', 'A').replace('D', 'K').replace('C', 'Q').replace('B', 'J').replace('A', 'T')

      
# calculate sum
l = len(final)
s = 0
for e in final:
    s += int(e[1]) * l
    l-=1

print(f"Part2: {s}")