from pathlib import Path
import json, re

fname = Path(__file__).absolute().parents[1] / 'inputs' / Path(__file__).name[3:5]
with open(fname.with_suffix(".txt"), "r") as f:
    rules, parts = f.read().split('\n\n')

# further parse the inputs
parts = [json.loads(x.replace('{', '{"').replace('=', '":').replace(',', ',"')) for x in parts.splitlines()]
tmp = {}
for x in rules.splitlines():
    tmp[x.split('{')[0]] = x.split('{')[1].replace('}','').split(',') 
rules = tmp

# recurse until we get either A, R
def get_part_result(x,m,a,s, rule):
    if isinstance(rule, str):
        return rule
    for r in rule[:-1]:
        cond, next_rule = r.split(':')
        if eval(cond):
            return get_part_result(x,m,a,s, rules.get(next_rule, next_rule))
    return get_part_result(x,m,a,s, rules.get(rule[-1], rule[-1]))
       
rule, s = "in", 0
for part in parts:
    if get_part_result(part["x"], part["m"], part["a"], part["s"], rules[rule]) == "A":
        s += sum(part.values())

print(f"Part1: {s}")

############################ Part2 ############################

def find_paths(rule, l, gather):
    l = l or []
    if rule in "AR":
        l.append(rule)
        gather.append(l)
        return
    r = rules[rule]
    for i in range(len(r)):
        tmp = l[:]
        # add negated prev conditions
        ttmp = []
        for j in range(0,i):
            if "<" in r[j]:
                ttmp.append(r[j].split(":")[0].replace("<", ">="))
            else:
                ttmp.append(r[j].split(":")[0].replace(">", "<="))
        if ":" not in r[i]:
            t = ' '.join(ttmp) + f":{r[i]}"
        else:
            ttmp.append(r[i])
            t = ' '.join(ttmp)
        idk, idc = t.rsplit(":", 1)
        tmp.append(idk)
        find_paths(idc, tmp, gather)

all_paths = []
find_paths("in", None, all_paths)
pass_paths = [x[:-1] for x in all_paths if x[-1] == "A"]

combinations = []
for path in pass_paths:
    all_conds = " ".join(path)
    x,m,a,s = [1, 4000], [1, 4000], [1, 4000], [1, 4000]
    for c in all_conds.split(' '):
        cond = re.split(r"(<=|>=|<|>)", c)
        if cond[1] == "<=":
            exec(f"{cond[0]}[1]=min({int(cond[2])}, {cond[0]}[1])")
        elif cond[1] == ">=":
            exec(f"{cond[0]}[0]=max({int(cond[2])}, {cond[0]}[0])")
        elif cond[1] == "<":
            exec(f"{cond[0]}[1]=min({int(cond[2])}-1, {cond[0]}[1])")
        elif cond[1] == ">":
            exec(f"{cond[0]}[0]=max({int(cond[2])}+1, {cond[0]}[0])")
    x,m,a,s = x[1] - x[0] + 1, m[1] - m[0] + 1, a[1] - a[0] + 1, s[1] - s[0] + 1
    combinations.append(x*m*a*s)

print(f"Part2: {sum(combinations)}")