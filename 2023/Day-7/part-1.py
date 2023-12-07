cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
cards.reverse()
hands_map = {}
with open("input") as f:
    for line in f:
        vals = line.split(" ")
        hands_map[vals[0]] = int(vals[1])

ranks = {
    "five": [],
    "four": [],
    "full": [],
    "three": [],
    "two": [],
    "one": [],
    "high": [],
}


def add_to_ranks(r, hand):
    if len(r) == 0:
        r.append(hand)
    else:
        flag = False
        rc = r[:]
        for i, x in enumerate(rc):
            for j in range(len(hand)):
                if hand[j] != x[j]:
                    if cards.index(hand[j]) > cards.index(x[j]):
                        r.insert(i, hand)
                        flag = True

                    break
            if flag:
                break

        if not flag:
            r.append(hand)


hands = list(hands_map.keys())
for hand in hands:
    d = {}
    for x in hand:
        d[x] = (d.get(x) or 0) + 1

    if len(d.keys()) == 1:
        add_to_ranks(ranks["five"], hand)
    elif 4 in list(d.values()):
        add_to_ranks(ranks["four"], hand)
    elif len(d.keys()) == 2 and 3 in list(d.values()):
        add_to_ranks(ranks["full"], hand)
    elif len(d.keys()) == 3 and 3 in list(d.values()):
        add_to_ranks(ranks["three"], hand)
    elif list(d.values()).count(2) == 2:
        add_to_ranks(ranks["two"], hand)
    elif len(d.keys()) == 4:
        add_to_ranks(ranks["one"], hand)
    elif len(d.keys()) == 5:
        add_to_ranks(ranks["high"], hand)

m = len(hands)
sum = 0
for k, v in ranks.items():
    for x in v:
        sum += hands_map[x] * m
        m -= 1

print(sum)
