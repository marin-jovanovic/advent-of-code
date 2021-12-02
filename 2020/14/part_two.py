def decimalToBinary(n):
    return bin(n).replace("0b", "")

def transform(data):
    pass




file = open("input.txt", "r")
raw_input = list()

[raw_input.append(i[:-1]) for i in file.readlines()]

prev_mask = None

from collections import defaultdict
main_d = {}

for elem in raw_input:
    # print(elem)

    if elem.startswith("mem"):
        t = elem.split(" ")
        new_v = int(t[2])
        f = int(t[0][4:-1])
        t = decimalToBinary(f).zfill(36)
        print(t)
        print(prev_mask)
        print("+ =")

        r_l= []
        x_d = []

        c =0
        for f, s in zip(prev_mask, t):
            # print(f, s)
            f = str(f)
            s = str(s)
            if f == "0" and s == "0":
                r_l.append(f)
            elif f == "1" and s == "0":
                r_l.append("1")
            elif f == "X" and s == "0":
                x_d.append(c)
                r_l.append("X")
            elif f == "0" and s == "1":
                r_l.append("1")
            elif f == "1" and s == "1":
                r_l.append("1")
            elif f == "X" and s == "1":
                r_l.append("X")
                x_d.append(c)
            # print("".join(r_l))
            c += 1

        tmp  = "".join(r_l)
        n_l = []
        print(tmp)
        t_2 = 2 **len(x_d)
        print(t_2)

        print()
        for i in range(t_2):
            n_l.append(tmp)

        t = []
        for i in range(t_2):
            b = bin(i)[2:]
            t.append(b)
        max_l = len(t[-1])

        n_t= []
        for i in t:
            if not len(i) == max_l:
                i = i.zfill(max_l)

            n_t.append(i)

        n = []
        for f, s in zip (n_t, n_l):
            for i in f:
                s = s.replace("X", i, 1)
            n.append(s)

        # [print(i) for i in n]
        for i in n:
            t = int(i,2)
            print(t)
            main_d[t] = new_v
        print(main_d)
    else:
        t = elem.split(" ")
        prev_mask = t[2]

print(sum(main_d.values()))