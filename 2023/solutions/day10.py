from pathlib import Path

fname = Path(__file__).absolute().parents[1] / 'inputs' / Path(__file__).name[3:5]
with open(fname.with_suffix(".txt"), "r") as f:
    m = f.read().splitlines()

def find_start_surr(n):
    # find possible exists from start
    surrounds = []
    #up
    if 0 <= n.x -1 < len(m) and m[n.x-1][n.y] in "|7FS":
        surrounds.append((n.x-1, n.y))
    #down
    if 0 <= n.x+1 < len(m) and m[n.x+1][n.y] in "|JLS":
        surrounds.append((n.x+1, n.y))
    #left
    if 0 <= n.y-1 < len(m[0]) and m[n.x][n.y-1] in "-LFS":
        surrounds.append((n.x, n.y-1))
    #right
    if 0 <= n.y+1 < len(m[0]) and m[n.x][n.y+1] in "-J7S":
        surrounds.append((n.x, n.y+1))
    return surrounds

def find_surr(n):
    # find possible exists from start
    surrounds = []
    if m[n.x][n.y] == "|":
        return [(n.x-1, n.y), (n.x+1, n.y)]
    elif m[n.x][n.y] == "-":
        return [(n.x, n.y-1), (n.x, n.y+1)]
    elif m[n.x][n.y] == "L":
        return [(n.x-1, n.y), (n.x, n.y+1)]
    elif m[n.x][n.y] == "J":
        return [(n.x-1, n.y), (n.x, n.y-1)]
    elif m[n.x][n.y] == "7":
        return [(n.x, n.y-1), (n.x+1,n.y)]
    elif m[n.x][n.y] == "F":
        return [(n.x, n.y+1), (n.x+1, n.y)]
    else:
        print(m[n.x][n.y])
        raise ValueError("wtf")

# build binary tree
class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next = None
        self.prev = None

    # Traversing and Displaying each element of the list
    def Display(self):
        n = self
        while True:
            print(f"{n.x, n.y} <-> ", end="")
            n = n.next
            if n.x == self.x and n.y == self.y:
                break
        print(f"{self.x, self.y}\n")

    def find_distance(self):
        n = self
        i = 0
        while True:
            i += 1
            n = n.next
            if n.x == self.x and n.y == self.y:
                break
        return i           

# find start
for i in range(len(m)):
    for j in range(len(m[i])):
        if "S" in m[i][j]:
            start = Node(i,j)


# find possible exists from start
s = find_start_surr(start)
assert len(s) == 2

start.next = Node(s[0][0], s[0][1])
start.prev = Node(s[1][0], s[1][1])
start.next.prev = start.prev.prev = start

current = start
allx, ally = [start.x], [start.y]
while True:
    # find two ways from next node
    current = current.next
    if current.x == start.x and current.y == start.y:
        break
    allx.append(current.x)
    ally.append(current.y)
    s = list(set(find_surr(current)) - set([(current.prev.x, current.prev.y)]))
    assert len(s) == 1
    current.next = Node(s[0][0], s[0][1])
    current.next.prev = current
    i +=1
    
print(f"Part1: {start.find_distance() / 2}")

####################### Part 2 #######################

import numpy as np
import skimage as ski
r, c = np.array(allx), np.array(ally)
rr, cc = ski.draw.polygon(r, c)
img = np.zeros((len(m), len(m[0])), dtype=int)
img[rr, cc] = 1
c = np.count_nonzero(img) - len(allx)
print(f"Part2: {c}")