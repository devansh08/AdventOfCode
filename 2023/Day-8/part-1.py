import re

steps = []
dirs = {}
with open("input") as f:
    for i, line in enumerate([x for x in [l.strip() for l in f] if x]):
        if i == 0:
            steps = list(map(lambda x: 0 if x == "L" else 1, line))
        else:
            l, r = line.split(" = ")
            dirs[l] = {k: v for (k, v) in zip([0, 1], re.findall("[A-Z]+", r))}

curr = "AAA"
i = 0
c = 0
while curr != "ZZZ":
    curr = dirs[curr][steps[i]]
    i = (i + 1) % len(steps)
    c += 1

print(c)
