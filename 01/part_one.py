file = open("input.txt", "r")
lines = list()

[lines.append(int(i[:-1])) for i in file.readlines()]

[
    [
        [print(lines[i] * lines[j]) if lines[i] + lines[j] == 2020 else False]
            for j in range(i, len(lines))
    ]
        for i in range(len(lines))
]