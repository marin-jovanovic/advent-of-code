print(
    sum(
        len(set(line.replace("\n", ""))) for line in open("input.txt").read().split("\n\n")
    )
)
