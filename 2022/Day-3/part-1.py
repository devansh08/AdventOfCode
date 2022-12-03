lines = open("input").readlines()

score = 0
for line in lines:
    c = list(set(line[: int(len(line) / 2)]) & set(line[int(len(line) / 2) :]))[0]

    if ord(c) >= ord("a"):
        score += ord(c) - ord("a") + 1
    else:
        score += ord(c) - ord("A") + 27

print(score)
