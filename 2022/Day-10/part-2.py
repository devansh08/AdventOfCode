lines = [l.strip("\n") for l in open("input").readlines()]

clk = 1
x = 1
i = 0
addFlag = False
s = 0
rows = [""]
row = 0
px = 0
while i < len(lines):
    if clk != 1 and clk % 40 == 1:
        px = 0
        row += 1
        rows.append("")

    rows[row] += "#" if px in [x - 1, x, x + 1] else "."

    op, *n = lines[i].split(" ")

    if op == "addx":
        if addFlag:
            addFlag = False
            x += int(n[0])
            i += 1
        else:
            addFlag = True
    else:
        i += 1

    clk += 1
    px += 1

for row in rows:
    print(row)
