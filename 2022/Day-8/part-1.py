grid = []

for line in open("input").readlines():
    grid.append([c for c in line.strip("\n")])

rows = len(grid[0])
cols = len(grid)

v = cols * 2 + 2 * (rows - 2)

for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        left = True
        right = True
        up = True
        down = True

        h = grid[i][j]

        for t, x in enumerate(grid[i]):
            if left and t < j and x >= h:
                left = False
            elif right and t > j and x >= h:
                right = False

        if left or right:
            v += 1
        else:
            for t, x in enumerate([r[j] for r in grid]):
                if up and t < i and x >= h:
                    up = False
                elif down and t > i and x >= h:
                    down = False

            if up or down:
                v += 1

print(v)
