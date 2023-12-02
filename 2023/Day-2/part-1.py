color_max = {"red": 12, "green": 13, "blue": 14}
sum = 0

with open("input") as f:
    for line in [l for l in [x.strip() for x in f] if l]:
        id, cubes = line.split(":")
        id = int(id.split(" ")[1])

        flag = True
        for set in cubes.split(";"):
            colors = [l.strip() for l in set.strip().split(",")]

            for color in colors:
                n, c = color.split(" ")

                if int(n) > color_max[c]:
                    flag = False
                    break

            if not flag:
                break

        if flag:
            sum += id

print(sum)
