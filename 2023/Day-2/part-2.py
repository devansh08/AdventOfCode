from functools import reduce

sum = 0

with open("input") as f:
    for line in [l for l in [x.strip() for x in f] if l]:
        _, cubes = line.split(":")

        colors_min = {"red": 0, "green": 0, "blue": 0}
        for subset in cubes.split(";"):
            colors = [
                [x for x in l.strip().split(" ")] for l in subset.strip().split(",")
            ]

            for color in colors:
                colors_min[color[1]] = max(int(color[0]), colors_min[color[1]])

        sum += reduce(lambda a, v: a * v, colors_min.values())

print(sum)
