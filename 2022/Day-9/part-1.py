lines = open("input").readlines()

visit = set()
visit.add((0, 0))
x, y = (0, 0)
a, b = (0, 0)
for line in lines:
    dir, c = line.strip("\n").split(" ")

    for i in range(int(c)):
        match dir:
            case "L":
                x -= 1
            case "R":
                x += 1
            case "U":
                y -= 1
            case "D":
                y += 1

        if ((x == a and y == b) or (abs(x - a) <= 1 and abs(y - b) <= 1)) is False:
            if x - a == 0:
                if y - b > 0:
                    b += 1
                else:
                    b -= 1
            elif y - b == 0:
                if x - a > 0:
                    a += 1
                else:
                    a -= 1
            else:
                if x - a > 0 and y - b > 0:
                    a += 1
                    b += 1
                elif x - a > 0 and y - b < 0:
                    a += 1
                    b -= 1
                elif x - a < 0 and y - b > 0:
                    a -= 1
                    b += 1
                elif x - a < 0 and y - b < 0:
                    a -= 1
                    b -= 1

        visit.add((a, b))

print(len(visit))
