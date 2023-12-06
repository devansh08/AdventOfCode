import re
import math

with open("input") as f:
    lines = f.readlines()

    time = [int(x) for x in re.findall("[0-9]+", lines[0])]
    dist = [int(x) for x in re.findall("[0-9]+", lines[1])]

prod = 1
for i, t in enumerate(time):
    x = (t + math.sqrt((t**2) - (4 * 1 * dist[i]))) / (2 * 1)
    y = (t - math.sqrt((t**2) - (4 * 1 * dist[i]))) / (2 * 1)

    prod *= int(math.fabs(math.ceil(y) - math.ceil(x)))

print(prod)
