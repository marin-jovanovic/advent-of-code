file = open("input.txt", "r")
lines = list()

[lines.append(i[:-1]) for i in file.readlines()]

f_l = [int(i) for i in lines[0].split(",")]
print(f_l)
# f_l

b = []
t = []

for line in lines[2:]:
    # print(line)
    l = [i for i in line.split(" ") if i != ""]

    if l == []:
        b.append([[int(j) for j in i] for i in t])
        t = []
    else:
        t.append(l)
b.append([[int(j) for j in i] for i in t])

l = 0
for i in t[0]:
    l += 1
print("l", l)

[print(i) for i in b]

print()

s_f = False

def get_transposed(a):

    print(a)

    [print(i) for i in a]

    off = 0
    l = []
    tmp = []

    from collections import defaultdict
    d = defaultdict(list)

    ln = len([i for i in a[0]])

    print(ln)
    for x in a:
        for off in range(ln):
            # print(off)
            d[off].append(x[off])

    [print(k,v) for k,v in d.items()]

    for k,v in d.items():
        print(v)

        if v == [None for i in range(ln)]:
            print("sve None")
            return  True

    return False

win_tbl = []
win_num = None

for i in f_l:
    print(i)
    tmp_2 = []
    for tbl in b:

        tmp = []
        for x in tbl:
            x = [None if j == i else j for j in x]
            tmp.append(x)
        tbl = tmp
        tmp_2.append(tbl)

    b = tmp_2

    # check for win
    for tbl in b:
        for x in tbl:
            if x == [None for i in tbl]:
                print("winner")
                s_f = True
                win_tbl = tbl

    if s_f:
        win_num = i
        break

    for tbl in b:
        if get_transposed(tbl):
            print("winner")
            s_f = True
            win_tbl = tbl
        if s_f:
            win_num = i
            break
    if s_f:
        win_num = i
        break

    [print(i) for i in b]

[print(i) for i in win_tbl]
s = 0
for x in win_tbl:
    s += sum([i for i in x if i])
print("s", s)
print(s * win_num)