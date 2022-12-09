lines = open("input").readlines()

visit = []
knots = [[0, 0] for i in range(10)]
for line in lines:
    dir, c = line.strip("\n").split(" ")

    for i in range(int(c)):
        match dir:
            case "L":
                knots[0][0] -= 1
            case "R":
                knots[0][0] += 1
            case "U":
                knots[0][1] -= 1
            case "D":
                knots[0][1] += 1

        for j in range(1, 10):
            if (
                (knots[j - 1][0] == knots[j][0] and knots[j - 1][1] == knots[j][1])
                or (
                    abs(knots[j - 1][0] - knots[j][0]) <= 1
                    and abs(knots[j - 1][1] - knots[j][1]) <= 1
                )
            ) is False:
                if knots[j - 1][0] - knots[j][0] == 0:
                    if knots[j - 1][1] - knots[j][1] > 0:
                        knots[j][1] += 1
                    else:
                        knots[j][1] -= 1
                elif knots[j - 1][1] - knots[j][1] == 0:
                    if knots[j - 1][0] - knots[j][0] > 0:
                        knots[j][0] += 1
                    else:
                        knots[j][0] -= 1
                else:
                    if (
                        knots[j - 1][0] - knots[j][0] > 0
                        and knots[j - 1][1] - knots[j][1] > 0
                    ):
                        knots[j][0] += 1
                        knots[j][1] += 1
                    elif (
                        knots[j - 1][0] - knots[j][0] > 0
                        and knots[j - 1][1] - knots[j][1] < 0
                    ):
                        knots[j][0] += 1
                        knots[j][1] -= 1
                    elif (
                        knots[j - 1][0] - knots[j][0] < 0
                        and knots[j - 1][1] - knots[j][1] > 0
                    ):
                        knots[j][0] -= 1
                        knots[j][1] += 1
                    elif (
                        knots[j - 1][0] - knots[j][0] < 0
                        and knots[j - 1][1] - knots[j][1] < 0
                    ):
                        knots[j][0] -= 1
                        knots[j][1] -= 1

        visit.append([knots[9][0], knots[9][1]])

print(len(set([(p[0], p[1]) for p in visit])))
