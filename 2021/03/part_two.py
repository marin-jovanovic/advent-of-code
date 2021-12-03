def new_filter(lines, index, inverted):
    c = 0
    c_1 = 0
    for i in lines:
        c += 1
        if i[index] == "1":
            c_1 += 1

    if c_1 + c_1 >= c:
        print("get 1")
        if inverted:
            f_v = "0"
        else:
            f_v = "1"

    else:
        if inverted:
            f_v = "1"
        else:
            f_v = "0"

    n_l = []
    for i in lines:
        if i[index] == f_v:
            n_l.append(i)

    return n_l


if __name__ == '__main__':

    l = []
    filename = "input.txt"

    lines = []
    for line in open(filename, "r").readlines():
        line = line[:-1]
        lines.append(line)

    a_l = [i for i in lines]
    b_l = [i for i in lines]
    i  = 0
    while True:
        a_l = new_filter(a_l, i, False)
        i += 1
        if len(a_l) == 1:
            break
    i  = 0

    while True:
        b_l = new_filter(b_l, i, True)
        i += 1
        if len(b_l) == 1:
            break

    print(int(a_l[0], 2) * int(b_l[0], 2))