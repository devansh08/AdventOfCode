max = 0
sum = 0

for cals in open("input").readlines():
    if cals.strip("\n") == "":
        if sum > max:
            max = sum

        sum = 0
    else:
        sum += int(cals.strip("\n"))

print(max)
