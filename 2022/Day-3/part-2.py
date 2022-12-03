from functools import reduce

lines = open("input").readlines()

print(
    reduce(
        lambda score, c: score + ord(c) - ord("a") + 1
        if ord(c) >= ord("a")
        else score + ord(c) - ord("A") + 27,
        list(
            zip(
                *[
                    sorted(reduce(lambda a, b: set(a) & set(b), l))
                    for l in [
                        lines[(i - 1) * 3 : i * 3]
                        for i in range(1, int(len(lines) / 3) + 1)
                    ]
                ]
            )
        )[1],
        0,
    )
)
