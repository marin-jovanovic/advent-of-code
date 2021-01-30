lines = [int(line[:-1]) for line in open("input.txt").readlines()]

[print(line) for line in lines]


def test(lst, num):
    for x in lst:
        for y in lst:
            if x + y == num and lst.index(x) != lst.index(y):
                return "= " + str(x) + " + " + str(y)
                return True

    print("no match for " + str(num))
    import sys
    sys.exit()


preamble = 25

for i in range(0, len(lines) - preamble):
    window = lines[i:preamble + i]
    target = lines[preamble + i]

    print(window, target, test(window, target))
