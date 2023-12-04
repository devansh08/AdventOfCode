import re

sum = 0
with open("input") as f:
    for line in f:
        if line and line != "\n":
            nums = list(
                re.finditer("Card\ +([0-9]+)\ :\ ([0-9\ ]+)\ |\ ([0-9\ ]+)", line)
            )

            win = [int(x) for x in nums[1].group().strip().split(" ") if x]
            num = [int(x) for x in nums[2].group().strip().split(" ") if x]

        c = 0
        for i in win:
            if i in num:
                c += 1

        if c != 0:
            sum += 2 ** (c - 1)

print(sum)
