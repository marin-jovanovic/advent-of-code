raw_input_lines = open("input.txt").read().split("\n")[:-1][0].split(",")
raw_input_lines = [int(i) for i in raw_input_lines]
print(raw_input_lines)

o = raw_input_lines

for num in range(80):
    n = []
    c_n = []

    for i in o:
        if i == 3:
            n.append(2)
        elif i == 2:
            n.append(1)
        elif i == 0:
            n.append(6)
            c_n.append(8)
        elif i == 6:
            n.append(5)
        elif i == 8:
            n.append(7)
        else:
            n.append(i - 1)


    o = n + c_n
    # print(num + 1, o)
    print(len(o))