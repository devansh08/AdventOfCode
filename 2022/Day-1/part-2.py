elves = []
total = 0

for cals in open("input").readlines():
    if cals.strip("\n") == "":
        elves.append(total)
        total = 0
    else:
        total += int(cals.strip("\n"))

print(sum(sorted(elves, reverse=True)[0:3]))
