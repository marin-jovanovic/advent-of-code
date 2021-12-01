def log(*data):
    return
    print(str(data))


lines = [line[:-1] for line in open("input.txt").readlines()]

[print(line) for line in lines]
print("->")


def make_test():
    test = list()

    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if x == i and y == j:
                continue

            if x < 0 or y < 0:
                continue

            try:
                test.append(lines[x][y])
            except:
                pass

    return test


control = list()

while lines != control:
    control = lines
    new_list = list()

    for i, line in enumerate(lines):
        log(i, line)

        new_line = ""

        for j, token in enumerate(line):
            log(j, token)

            if token == "L":

                test = make_test()

                if not test.__contains__("#"):
                    new_line += "#"
                else:
                    new_line += "L"
                log(test)

            elif token == "#":

                test = make_test()

                if test.count("#") >= 4:
                    new_line += "L"
                else:
                    new_line += "#"
                log(test)

            else:
                new_line += "."

        new_list.append(new_line)

    lines = new_list

    [print(line) for line in lines]
    print("->")

print(sum([line.count("#") for line in lines]))
