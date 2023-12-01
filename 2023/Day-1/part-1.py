import re

reg = re.compile("[0-9]")

sum = 0
with open("input") as f:
    for line in [l for l in [l.strip() for l in f] if l]:
        matches = reg.findall(line.strip("\n"))
        a, b = matches[0], matches[-1]

        sum += int(a + b)

print(sum)
