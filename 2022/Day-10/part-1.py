lines = [l.strip("\n") for l in open("input").readlines()]

clk = 1
cycles = [20 * i for i in range(1, int(len(lines) / 10)) if i % 2 == 1]
x = 1
i = 0
addFlag = False
s = 0
while i < len(lines):
    if clk in cycles:
        s += clk * x

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

print(s)
