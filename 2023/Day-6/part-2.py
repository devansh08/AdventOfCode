import re
import math

with open("input") as f:
    lines = f.readlines()

    time = int("".join([x for x in re.findall("[0-9]+", lines[0])]))
    dist = int("".join([x for x in re.findall("[0-9]+", lines[1])]))

x = (time + math.sqrt((time**2) - (4 * 1 * dist))) / (2 * 1)
y = (time - math.sqrt((time**2) - (4 * 1 * dist))) / (2 * 1)

print(int(math.fabs(math.ceil(y) - math.ceil(x))))
