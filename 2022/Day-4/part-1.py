print(
    len(
        list(
            filter(
                lambda x: (
                    (x[0][0] <= x[1][0] and x[0][1] >= x[1][1])
                    or (x[0][0] >= x[1][0] and x[0][1] <= x[1][1])
                ),
                [
                    (
                        [int(i) for i in x[0].split("-")],
                        [int(i) for i in x[1].split("-")],
                    )
                    for x in [
                        line.strip("\n").split(",")
                        for line in open("input").readlines()
                    ]
                ],
            )
        )
    )
)
