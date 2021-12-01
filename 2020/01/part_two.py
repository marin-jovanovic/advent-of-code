file = open("input.txt", "r")
lines = list()

[lines.append(int(i[:-1])) for i in file.readlines()]


for i in range(len(lines)):
    for j in range(i, len(lines)):
        for k in range(j, len(lines)):
            [print(lines[i] * lines[j] * lines[k])
             if lines[i] + lines[j] + lines[k] == 2020 else False]
