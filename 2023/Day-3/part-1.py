import re

arr = []
sum = 0
with open("input") as f:
    for line in [l for l in [x.strip() for x in f] if l]:
        arr.append(line)

for i, line in enumerate(arr):
    for num_match in [x for x in re.finditer("[0-9]+", line)]:
        start, end = num_match.span()
        num = num_match.group()

        indices = {
            (x, y)
            for x in (max(i - 1, 0), i, min(i + 1, len(line) - 1))
            for y in range(max(start - 1, 0), min(end + 1, len(line)))
        }

        for x, y in indices:
            if arr[x][y] not in "1234567890.":
                sum += int(num)
                break

print(sum)
