import re

num_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

reg = re.compile("(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))")

sum = 0
with open("input") as f:
    for line in [l for l in [l.strip() for l in f] if l]:
        matches = reg.findall(line.strip("\n"))
        a, b = (
            num_dict.get(matches[0]) or matches[0],
            num_dict.get(matches[-1]) or matches[-1],
        )

        sum += int(a + b)

print(sum)
