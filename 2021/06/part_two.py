raw_input_lines = open("input.txt").read().split("\n")[:-1][0].split(",")
raw_input_lines = [int(i) for i in raw_input_lines]
print(raw_input_lines)

from collections import defaultdict
o = defaultdict(int)
for i in raw_input_lines:
    o[i] += 1


for num in range(256):
    n = defaultdict(int)
    # c_n = []
    n_d = defaultdict(int)

    for i,v in o.items():
        # print(i,v)

        if i == 3:
            n[2] += v

        elif i == 2:
            n[1] += v

        elif i == 0:
            n[6] += v
            n[8] += v

        elif i == 6:
            n[5] += v

        elif i == 8:
            n[7] += v

        else:
            n[i-1] += v

    o = n
    c = 0
    for i,v in o.items():
        c +=  v
    print("=",num + 1, c)

    # print(c_n)
    print()
