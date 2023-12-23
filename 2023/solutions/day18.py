from pathlib import Path

fname = Path(__file__).absolute().parents[1] / 'inputs' / Path(__file__).name[3:5]
with open(fname.with_suffix(".txt"), "r") as f:
    moves = list(map(str.split, f.read().splitlines()))

# find all edge points
points, B = [(0, 0)], 0
for move in moves:
    dist = int(move[1])
    B += dist
    if move[0] == "R":
        points.append((points[-1][0], points[-1][1] + dist))
    elif move[0] == "L":
        points.append((points[-1][0], points[-1][1] - dist))
    elif move[0] == "U":
        points.append((points[-1][0] - dist, points[-1][1]))
    elif move[0] == "D":
        points.append((points[-1][0] + dist, points[-1][1]))

# Solution: Gauss area + Pick's theorem
# 1. find Area of the polygon
# 2. Use Pick's theorem to calculate amount of points inside polygon
A =  abs(sum([points[i][0]*points[i+1][1] - points[i+1][0]*points[i][1] for i in range(len(points) - 1)])) // 2
I = A - (B // 2) + 1
print(f"Part1: {I + B}")

############################ Part2 ############################

# find all edge points
points, B = [(0, 0)], 0
for move in moves:
    dist = int(move[2][2:7], 16)
    dir = int(move[2][7:8])
    B += dist
    if dir == 0:
        points.append((points[-1][0], points[-1][1] + dist))
    elif dir == 2:
        points.append((points[-1][0], points[-1][1] - dist))
    elif dir == 3:
        points.append((points[-1][0] - dist, points[-1][1]))
    elif dir == 1:
        points.append((points[-1][0] + dist, points[-1][1]))

# Solution: Gauss area + Pick's theorem
# 1. find Area of the polygon
# 2. Use Pick's theorem to calculate amount of points inside polygon
A =  abs(sum([points[i][0]*points[i+1][1] - points[i+1][0]*points[i][1] for i in range(len(points) - 1)])) // 2
I = A - (B // 2) + 1
print(f"Part2: {I + B}")