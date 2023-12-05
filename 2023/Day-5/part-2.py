seeds = []
maps = []
with open("input") as f:
    j = -1
    for i, line in enumerate(f):
        if line.strip() != "":
            if i == 0:
                seed_list = [int(x) for x in line.split(":")[1].split(" ") if x]
                for i, x in enumerate(seed_list):
                    if i % 2 == 0:
                        seeds.append(range(x, x + seed_list[i + 1]))
            else:
                if line[0].isnumeric():
                    val, key, inc = [int(x) for x in line.split(" ") if x]
                    maps[j][range(key, key + inc)] = range(val, val + inc)
                else:
                    j += 1
                    maps.append({})

vals = []
for seed_rng in seeds:
    val = [seed_rng]
    for j in range(len(maps)):
        m = sorted(maps[j].keys(), key=lambda x: x.start)

        new_val = []
        for rng in val:
            flag = len(new_val)
            start, stop = rng.start, rng.stop
            for k in m:
                no_break = False

                if stop < k.start or start > k.stop:
                    pass
                elif start < k.start and stop > k.stop:
                    new_val.append(range(start, k.start))
                    new_val.append(maps[j][k])

                    start = k.stop
                    no_break = True
                elif start < k.start and stop <= k.stop:
                    new_val.append(range(start, k.start))
                    new_val.append(
                        range(maps[j][k].start, maps[j][k].start + (stop - k.start))
                    )

                    break
                elif start >= k.start and stop > k.stop:
                    new_val.append(
                        range(maps[j][k].start + (start - k.start), maps[j][k].stop)
                    )

                    start = k.stop
                    no_break = True
                elif start >= k.start and stop <= k.stop:
                    new_val.append(
                        range(
                            maps[j][k].start + (start - k.start),
                            maps[j][k].stop - (k.stop - stop),
                        )
                    )

                    break

            if len(new_val) == flag:
                new_val.append(rng)

            if no_break:
                new_val.append(range(start, stop))

        val = sorted(new_val, key=lambda x: x.start)[:]

    vals.append(val)

print(sorted([x[0] for x in vals], key=lambda x: x.start)[0].start)
