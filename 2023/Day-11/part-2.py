maze = []
with open("input") as f:
    for line in f:
        maze.append([x for x in line.strip()])


def transpose_maze(maze):
    for i in range(len(maze)):
        for j in range(i, len(maze)):
            maze[i][j], maze[j][i] = maze[j][i], maze[i][j]

    return maze


def find_empty_rows(maze):
    r = []
    for i, row in enumerate(maze):
        if row.count("#") == 0:
            r.append(i)

    return r


row = find_empty_rows(maze)
maze = transpose_maze(maze)

col = find_empty_rows(maze)
maze = transpose_maze(maze)

gl = []
for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] == "#":
            gl.append((i, j))

s = 0
for i in range(len(gl)):
    for j in range(i, len(gl)):
        if i != j:
            ax, ay = gl[i]
            bx, by = gl[j]

            x = range(*sorted([ax, bx]))
            y = range(*sorted([ay, by]))

            val = 1000000 - 1
            rc = 0
            for r in row:
                if r in x:
                    rc += 1

            s += abs(ax - bx) + rc * val

            cc = 0
            for c in col:
                if c in y:
                    cc += 1

            s += abs(ay - by) + cc * val

print(s)
