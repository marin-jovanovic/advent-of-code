raw_input_lines = open("input.txt").read().split("\n")[:-1]


r  = []
t = []


[print(i) for i in r]

from collections import defaultdict
r_d = defaultdict(int)

for i in raw_input_lines:

    i = i.split(" ")
    l = [int(j) for j in i[0].split(",")]
    r = [int(j) for j in i[2].split(",")]

    print(l,r)

    if l[0] == r[0]:
        # print("l")

        for num in range(min(l[1], r[1]), max(l[1] + 1, r[1] +1)):
            r_d[(l[0], num)] += 1

        # for k, v in r_d.items():
        #     print(k, v)

    elif l[1] == r[1]:
        # print("r")

        for num in range(min(l[0], r[0]), max(l[0] + 1, r[0] +1)):
            r_d[(num, l[1])] += 1

        # for k, v in r_d.items():
        #     print(k, v)

    else:
        # print()

        if l[0] > r[0] and l[1] > r[1]:
            print(1)
            for off in range(0, abs(l[0] - r[0]) + 1):
                print(r[0] + off, r[1] + off)
                r_d[(r[0] + off, r[1] + off)] += 1

        elif l[0] > r[0] and l[1] < r[1]:
            print(2)
            for off in range(0, abs(l[0] - r[0]) + 1):
                print(- r[0] + off, r[1] - off)
                r_d[(r[0] + off, r[1] - off)] += 1

        elif l[0] < r[0] and l[1] > r[1]:
            print(3)
            for off in range(0, abs(l[0] - r[0]) + 1):
                print(r[0] - off, r[1] + off)
                r_d[(r[0] - off, r[1] + off)] += 1

        elif l[0] < r[0] and l[1] < r[1]:
            print(4)
            for off in range(0, abs(l[0] - r[0]) + 1):
                print(r[0] - off, r[1] - off)
                r_d[(r[0] - off, r[1] - off)] += 1

c = 0


for k,v in r_d.items():
    print(k,v)
    if v >= 2:
        c += 1

# for i in range(9):

print(c)
