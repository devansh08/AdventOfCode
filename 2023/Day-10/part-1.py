maze = []
start = (0, 0)
dir_map = {
    (1, 0): {"-": (1, 0), "J": (0, -1), "7": (0, 1)},
    (0, 1): {"|": (0, 1), "L": (1, 0), "J": (-1, 0)},
    (-1, 0): {"-": (-1, 0), "L": (0, -1), "F": (0, 1)},
    (0, -1): {"|": (0, -1), "7": (-1, 0), "F": (1, 0)},
}

with open("input") as f:
    i = 0
    for line in f:
        maze_line = []
        j = 0
        for c in line.strip():
            if c == "S":
                start = (j, i)
            maze_line.append(c)

            j += 1

        maze.append(maze_line)
        i += 1


def is_valid(x, y):
    return x >= 0 and x < len(maze[0]) and y >= 0 and y < len(maze)


curr = start[:]
c = 0
while True:
    x, y = curr
    if maze[y][x] == ".":
        curr = start
        c = 0

    if curr == start:
        for dx, dy in list(dir_map.keys()):
            ptx, pty = (x + dx, y + dy)
            if (
                is_valid(ptx, pty)
                and (ch := maze[pty][ptx]) != "."
                and ch in list(dir_map[(dx, dy)].keys())
            ):
                nx, ny = dir_map[(dx, dy)][ch]
                curr = (ptx + nx, pty + ny)
                c += 1
    else:
        ch = maze[y][x]
        nx, ny = dir_map[(nx, ny)][ch]
        curr = (x + nx, y + ny)
        c += 1

    if curr == start and c > 0:
        break

print(c // 2)
