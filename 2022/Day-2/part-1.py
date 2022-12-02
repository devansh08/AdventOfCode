opponent, player = list(
    map(
        lambda x: (l := x[0], c := x[1])
        and list(map(lambda x, c=c: ord(x) - ord(c), l)),
        zip(
            zip(*[line.strip("\n").split(" ") for line in open("input").readlines()]),
            ["A", "X"],
        ),
    )
)

score = 0
for o, p in zip(opponent, player):
    if o == p:
        score += 3 + p + 1
    elif (o + 1) % 3 == p:
        score += 6 + p + 1
    else:
        score += p + 1

print(score)
