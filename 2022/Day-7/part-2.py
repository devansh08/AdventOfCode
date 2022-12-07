import re

lines = [l.strip("\n") for l in open("input").readlines()]

fs = {}
path = ""
cd = ""
for line in lines:
    if (temp := re.match(r"\$ cd (.+)", line)) is not None:
        d = temp.group(1)
        if d != "..":
            cd = d
            path += ("/" if path != "/" and path != "" else "") + d
        else:
            cd = path.split("/")[-1]
            path = "/".join(path.split("/")[:-1]) or "/"

        if path not in fs.keys():
            fs[path] = 0
    elif re.match(r"\$ ls", line) is None:
        if (temp := re.match(r"[0-9]+", line)) is not None:
            size = int(temp.group())
            spath = path

            fs[path] += size
            if path != "/":
                for i in range(len(path.split("/")) - 1):
                    spath = "/".join(spath.split("/")[:-1]) or "/"
                    fs[spath] += size

print(next(s for s in sorted(fs.values()) if s > 30000000 - (70000000 - fs["/"])))
