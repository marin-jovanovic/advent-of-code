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
        print("l")

        for num in range(min(l[1], r[1]), max(l[1] + 1, r[1] +1)):
            r_d[(l[0], num)] += 1

        # for k, v in r_d.items():
        #     print(k, v)

    elif l[1] == r[1]:
        print("r")

        for num in range(min(l[0], r[0]), max(l[0] + 1, r[0] +1)):
            r_d[(num, l[1])] += 1

        # for k, v in r_d.items():
        #     print(k, v)

    else:
        print("no match")

c = 0
for k,v in r_d.items():
    print(k,v)
    if v >= 2:
        c += 1

print(c)