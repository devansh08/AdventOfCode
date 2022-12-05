import re

lines = [l.strip("\n") for l in open("input").readlines()]

stackInputs = lines[0 : lines.index("")]
n = len(stackInputs[-1].split("   "))

stacks = {i: [] for i in range(1, n + 1)}
for line in lines[0 : lines.index("") - 1]:
    for i, x in enumerate(range(1, len(line), 4)):
        if line[x] != " ":
            stacks[i + 1].insert(0, line[x])

inputs = lines[lines.index("") + 1 :]

for line in inputs:
    [c, f, t] = [int(x) for x in re.findall(r"[0-9]+", line)]

    stacks[t].extend(stacks[f][-c:][::-1])
    stacks[f] = stacks[f][:-c]

s = ""
for l in stacks.values():
    s += l[-1]

print(s)
