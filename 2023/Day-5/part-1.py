seeds = []
maps = []
with open("input") as f:
    j = -1
    for i, line in enumerate(f):
        if line.strip() != "":
            if i == 0:
                seeds = [int(x) for x in line.split(":")[1].split(" ") if x]
            else:
                if line[0].isnumeric():
                    val, key, inc = [int(x) for x in line.split(" ") if x]
                    maps[j][range(key, key + inc)] = range(val, val + inc)
                else:
                    j += 1
                    maps.append({})

vals = []
for seed in seeds:
    val = seed
    for j in range(len(maps)):
        m = maps[j]

        for k in m.keys():
            if val in k:
                val = m[k].start + (val - k.start)
                break

    vals.append(val)

print(min(vals))
