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


def print_maze_item(x, y):
    c = maze[x][y]

    match c:
        case "F":
            c = "┌"
        case "J":
            c = "┘"
        case "L":
            c = "└"
        case "7":
            c = "┐"
        case "|":
            c = "│"
        case "-":
            c = "─"

    print(c, end="")


curr = start[:]
c = 0
path = []
while True:
    x, y = curr
    if maze[y][x] == ".":
        curr = start
        c = 0
        path = []

    if curr == start:
        for dx, dy in list(dir_map.keys()):
            ptx, pty = (x + dx, y + dy)
            if (
                is_valid(ptx, pty)
                and (ch := maze[pty][ptx]) != "."
                and ch in list(dir_map[(dx, dy)].keys())
            ):
                nx, ny = dir_map[(dx, dy)][ch]
                path.append((ptx, pty))

                curr = (ptx + nx, pty + ny)
                path.append(curr)
                
                c += 1
                
                break
    else:
        ch = maze[y][x]
        
        nx, ny = dir_map[(nx, ny)][ch]
        curr = (x + nx, y + ny)
        
        path.append(curr)

        c += 1

    if curr == start and c > 0:
        break

c += 1

inc = 0
for i in range(len(maze)):
    flag_up = False
    flag_dn = False

    for j in range(len(maze[0])):
        m = maze[i][j]

        if m == "S":
            a, b = path[0], path[-2]

            k = (start[0] - a[0], start[1] - a[1])
            v = (b[0] - start[0], b[1] - start[1])
            m = list(filter(lambda x: x[1] == v, list(dir_map[k].items())))[0][0]

        if (j, i) in path:
            if m == "|":
                flag_up = not flag_up
                flag_dn = not flag_dn
            else:
                if m in ("L", "J"):
                    flag_up = not flag_up
                elif m in ("F", "7"):
                    flag_dn = not flag_dn

        if (j, i) not in path and (flag_up or flag_dn):
            inc += 1

print(inc)
