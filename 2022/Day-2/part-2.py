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
    match p:
        case 0:
            score += (o + 2) % 3 + 1
        case 1:
            score += 3 + o + 1
        case 2:
            score += 6 + (o + 1) % 3 + 1

print(score)
