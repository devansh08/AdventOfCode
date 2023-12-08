import math
import re

steps = []
dirs = {}
with open("input") as f:
    for i, line in enumerate([x for x in [l.strip() for l in f] if x]):
        if i == 0:
            steps = list(map(lambda x: 0 if x == "L" else 1, line))
        else:
            l, r = line.split(" = ")
            dirs[l] = {k: v for (k, v) in zip([0, 1], re.findall("[A-Z0-9]+", r))}

nodes = []
for k in list(dirs.keys()):
    if k[-1] == "A":
        nodes.append(k)

i = 0
c = [0 for _ in range(len(nodes))]
while True:
    for j in range(len(nodes)):
        if nodes[j] != "":
            nodes[j] = dirs[nodes[j]][steps[i]]
            c[j] += 1

    i = (i + 1) % len(steps)

    flag = False
    for k, x in enumerate(nodes):
        if x != "":
            if x[-1] == "Z":
                nodes[k] = ""
            else:
                flag = True

    if not flag:
        break

print(math.lcm(*c))
