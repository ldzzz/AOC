import sys
from operator import itemgetter
from pathlib import Path

fname = Path(__file__).absolute().parents[1] / 'inputs' / Path(__file__).name[3:5]
with open(fname.with_suffix(".txt"), "r") as f:
    patterns = list(map(str.split, f.read().split('\n\n')))

s, sols = 0, []
sols = []
for pattern in patterns:
    # check if rows perfect mirror
    is_row = False
    for i in range(len(pattern)-1):
        if pattern[i] == pattern[i+1]:
            ii, jj = i, i+1
            while ii >= 0 and jj < len(pattern):
                if pattern[ii] != pattern[jj]:
                    break
                ii, jj = ii-1, jj+1
            else:
                sols.append({i: 'R'})
                is_row = True
                s += 100*(i+1)
    
    if not is_row:
        # find all columns and repeat
        cols = [''.join(list(map(itemgetter(i), pattern))) for i in range(len(pattern[0]))]
        for i in range(len(cols)-1):
            if cols[i] == cols[i+1]:
                ii, jj = i, i+1
                while ii >= 0 and jj < len(cols):
                    if cols[ii] != cols[jj]:
                        break
                    ii, jj = ii-1, jj+1
                else:
                    sols.append({i: 'C'})
                    s += i+1

print(f"Part1: {s}")

############################ Part2 ############################

s = k = 0
for pattern in patterns:
    is_row = False
    for i in range(len(pattern)-1):
        if pattern[i] == pattern[i+1]:
            ii, jj = i, i+1
            while ii >= 0 and jj < len(pattern):
                if pattern[ii] != pattern[jj]:
                    diffs = 0
                    for j in range(len(pattern[ii])):
                        if pattern[ii][j] != pattern[jj][j]:
                            diffs += 1
                    if diffs != 1:
                        break
                ii, jj = ii-1, jj+1
            else:
                if sols[k].get(i, None) == None or sols[k][i] != 'R':
                    is_row = True
                    s += 100*(i+1)
        else:
            diffs = 0
            for j in range(len(pattern[i])):
                if pattern[i][j] != pattern[i+1][j]:
                    diffs += 1
            if diffs == 1:
                ii, jj = i-1, i+2
                while ii >= 0 and jj < len(pattern):
                    if pattern[ii] != pattern[jj]:
                        diffs = 0
                        for j in range(len(pattern[ii])):
                            if pattern[ii][j] != pattern[jj][j]:
                                diffs += 1
                        if diffs != 1:
                            break
                    ii, jj = ii-1, jj+1
                else:
                    if sols[k].get(i, None) == None or sols[k][i] != 'R':
                        is_row = True
                        s += 100*(i+1)
        if is_row:
            break
    
    if not is_row:
        # find all columns and repeat
        cols = [''.join(list(map(itemgetter(i), pattern))) for i in range(len(pattern[0]))]
        is_col = False
        for i in range(len(cols)-1):
            if cols[i] == cols[i+1]:
                ii, jj = i, i+1
                while ii >= 0 and jj < len(cols):
                    if cols[ii] != cols[jj]:
                        diffs = 0
                        for j in range(len(cols[ii])):
                            if cols[ii][j] != cols[jj][j]:
                                diffs += 1
                        if diffs != 1:
                            break
                    ii, jj = ii-1, jj+1
                else:
                    if sols[k].get(i, None) == None or sols[k][i] != 'C':
                        is_col = True
                        s += i+1
            else:
                diffs = 0
                for j in range(len(cols[i])):
                    if cols[i][j] != cols[i+1][j]:
                        diffs += 1
                if diffs == 1:
                    ii, jj = i-1, i+2
                    while ii >= 0 and jj < len(cols):
                        if cols[ii] != cols[jj]:
                            diffs = 0
                            for j in range(len(cols[ii])):
                                if cols[ii][j] != cols[jj][j]:
                                    diffs += 1
                            if diffs != 1:
                                break
                        ii, jj = ii-1, jj+1
                    else:
                        if sols[k].get(i, None) == None or sols[k][i] != 'C':
                            is_col = True
                            s += i+1
            if is_col:
                break
    k += 1

print(f"Part2: {s}")