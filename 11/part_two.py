def log(*data):
    return
    print(str(data))


lines = [line[:-1] for line in open("input.txt").readlines()]

[print(line) for line in lines]
print("->")


def make_test():
    arr = list()

    for xer in range(-1, 2):
        for yer in range(-1, 2):
            if xer == yer == 0:
                continue
            x = i
            y = j
            try:
                while lines[x][y] == "." or (x == i and y == j):
                    x += xer
                    y += yer
                    if x < 0 or y < 0:
                        break
                    log(x, y, lines[x][y])

                if x < 0 or y < 0:
                    arr.append(".")
                else:
                    log("target", lines[x][y], x, y)
                    arr.append(lines[x][y])
            except IndexError:
                log("err")
                arr.append(".")
                pass

    log(arr)
    return arr


control = list()

while lines != control:
    control = lines
    new_list = list()

    for i, line in enumerate(lines):
        log(i, line)

        new_line = ""

        for j, token in enumerate(line):
            log(j, token)

            # test = list()


            if token == "L":

                test = make_test()

                if not test.__contains__("#"):
                    new_line += "#"
                else:
                    new_line += "L"
                log(test)

            elif token == "#":

                test = make_test()

                if test.count("#") >= 5:
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
