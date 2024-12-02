from pathlib import Path

fname = Path(__file__).absolute().parents[1] / 'inputs' / Path(__file__).name[3:5]
with open(fname.with_suffix(".txt"), "r") as f:
    grid = list(map(list, f.read().splitlines()))

def walker(pos, visited):
    while True:
        # out of bounds OR loop detected
        if not (0 <= pos[0] < len(grid) and 0<= pos[1] < len(grid[0])) or pos in visited:
            return visited
        visited.append(pos.copy())
        if grid[pos[0]][pos[1]] == '.':
            if pos[2] == "R":
                pos[1] += 1
            elif pos[2] == "L":
                pos[1] -= 1
            elif pos[2] == "U":
                pos[0] -= 1
            elif pos[2] == "D":
                pos[0] += 1
        elif grid[pos[0]][pos[1]] == '/':
            if pos[2] == "R":
                pos[0] -= 1
                pos[2] = "U"
            elif pos[2] == "L":
                pos[0] += 1
                pos[2] = "D"
            elif pos[2] == "U":
                pos[1] += 1
                pos[2] = "R"
            elif pos[2] == "D":
                pos[1] -= 1
                pos[2] = "L"
        elif grid[pos[0]][pos[1]] == '\\':
            if pos[2] == "R":
                pos[0] += 1
                pos[2] = "D"
            elif pos[2] == "L":
                pos[0] -= 1
                pos[2] = "U"
            elif pos[2] == "U":
                pos[1] -= 1
                pos[2] = "L"
            elif pos[2] == "D":
                pos[1] += 1
                pos[2] = "R"
        elif grid[pos[0]][pos[1]] == '-':
            if pos[2] == "R":
                pos[1] += 1
            elif pos[2] == "L":
                pos[1] -= 1
            elif pos[2] == "U":
                tmp = pos.copy()
                tmp[1] -= 1
                tmp[2] = "L"
                visited = walker(tmp, visited)
                pos[1] += 1
                pos[2] = "R"
            elif pos[2] == "D":
                tmp = pos.copy()
                tmp[1] -= 1
                tmp[2] = "L"
                visited = walker(tmp, visited)
                pos[1] += 1
                pos[2] = "R"
        elif grid[pos[0]][pos[1]] == '|':
            if pos[2] == "R":
                tmp = pos.copy()
                tmp[0] -= 1
                tmp[2] = "U"
                visited = walker(tmp, visited)
                pos[0] += 1
                pos[2] = "D"
            elif pos[2] == "L":
                tmp = pos.copy()
                tmp[0] -= 1
                tmp[2] = "U"
                visited = walker(tmp, visited)
                pos[0] += 1
                pos[2] = "D"
            elif pos[2] == "U":
                pos[0] -= 1
            elif pos[2] == "D":
                pos[0] += 1
        else:
            raise ValueError(f"Unexpected value: {pos}")

res = set([(x[0], x[1]) for x in walker([0,0, 'R'], [])])
print(f"Part1: {len(res)}")

############################ Part2 ############################

possibilities = []
for i in range(0, len(grid)):
    possibilities.append([0, i, "D"])
    possibilities.append([i, 0, "R"])
    possibilities.append([len(grid)-1, i, "U"])
    possibilities.append([i, len(grid)-1, "L"])

res = []
for e in possibilities:
    res.append(set([tuple(x[:2]) for x in walker([0,0, 'R'], [])]) )

print(f"Part2: {len(max(res))}")