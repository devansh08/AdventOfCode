grid = []

for line in open("input").readlines():
    grid.append([c for c in line.strip("\n")])

rows = len(grid[0])
cols = len(grid)

mscore = 1
for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        score = 1

        left = True
        right = True
        up = True
        down = True

        h = grid[i][j]

        for x in range(1, j if j >= (cols - j) else (cols - j)):
            tr = grid[i]
            if left and (j - x) >= 0 and tr[j - x] >= h:
                left = False
                score *= x
            elif right and (j + x) < cols and tr[j + x] >= h:
                right = False
                score *= x

        if left:
            score *= j
        if right:
            score *= cols - j - 1

        for y in range(1, i if i >= (rows - i) else (rows - i)):
            tc = [r[j] for r in grid]
            if up and (i - y) >= 0 and tc[i - y] >= h:
                up = False
                score *= y
            elif down and (i + y) < rows and tc[i + y] >= h:
                down = False
                score *= y

        if up:
            score *= i
        if down:
            score *= rows - i - 1

        if score > mscore:
            mscore = score

print(mscore)
