import re

card_score = {}
with open("input") as f:
    for line in f:
        if line and line != "\n":
            nums = list(
                re.finditer("Card\ +([0-9]+)\ :\ ([0-9\ ]+)\ |\ ([0-9\ ]+)", line)
            )

            id = int(nums[0].group().strip())
            win = [int(x) for x in nums[1].group().strip().split(" ") if x]
            num = [int(x) for x in nums[2].group().strip().split(" ") if x]

            c = 0
            for i in win:
                if i in num:
                    c += 1

            card_score[id] = c

cards = [1 for _ in range(id)]

values = list(card_score.values())
for i in range(1, id):
    for j in range(0, i):
        if values[j] > 0:
            values[j] -= 1
            cards[i] += cards[j]

print(sum(cards))
