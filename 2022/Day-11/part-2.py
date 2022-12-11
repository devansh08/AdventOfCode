from functools import reduce

lines = open("input").readlines()

monkeys = []
for i in range(int(len(lines) / 7) + 1):
    props = [line.strip() for line in lines[i * 7 : (i + 1) * 7]]

    monkeys.append(
        {
            "items": [int(n.strip()) for n in props[1].split(":")[1].split(",")],
            "op": props[2].split("old")[1].split(" ")[1],
            "factor": props[2].split("old")[1].split(" ")[2],
            "test": int(props[3].split("by")[1].strip()),
            "true": int(props[4].split("monkey")[1].strip()),
            "false": int(props[5].split("monkey")[1].strip()),
            "count": 0,
        }
    )

mod = reduce(lambda x, y: x * y, [monkey["test"] for monkey in monkeys])
for round in range(10000):
    for monkey in monkeys:
        for item in monkey["items"]:
            factor = int(monkey["factor"]) if monkey["factor"].isdigit() else item
            worry = int(item * factor if monkey["op"] == "*" else item + factor) % mod

            if worry % monkey["test"] == 0:
                monkeys[monkey["true"]]["items"].append(worry)
            else:
                monkeys[monkey["false"]]["items"].append(worry)

        monkey["count"] += len(monkey["items"])
        monkey["items"] = []

print(
    reduce(
        lambda x, y: x * y,
        sorted([monkey["count"] for monkey in monkeys], reverse=True)[:2],
    )
)
