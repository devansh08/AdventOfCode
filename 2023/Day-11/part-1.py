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
    row_i = []
    for i, row in enumerate(maze):
        if row.count("#") == 0:
            row_i.append(i + len(row_i))

    return row_i


row_i = find_empty_rows(maze)
maze = transpose_maze(maze)

row_j = find_empty_rows(maze)
maze = transpose_maze(maze)

for i in row_i:
    maze.insert(i, ["." for _ in range(len(maze[0]))])

for j in row_j:
    for i in range(len(maze)):
        maze[i].insert(j, ".")

gl = []
for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] == '#':
            gl.append((i, j))

s = 0
for i in range(len(gl)):
    for j in range(i, len(gl)):
        if i != j:
            s += (abs(gl[i][0] - gl[j][0]) + abs(gl[i][1] - gl[j][1]))

print(s)

