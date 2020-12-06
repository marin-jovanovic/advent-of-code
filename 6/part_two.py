# delete last empty line in input.txt

print(
    sum(
        [
            len(
                set(
                    "".join(
                        (i if line.count(i) == line.count("\n") + 1 else "") for i in line
                    )
                )
            ) for line in open("input.txt").read().split("\n\n")
        ]
    )
)
