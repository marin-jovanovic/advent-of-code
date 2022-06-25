lines = [line[:-1] for line in open("input.txt").readlines()]
# print(lines)

c = 0

def is_sub(big, small):
    return all(x in big for x in small)

for i in lines:
    tmp = i.split(" | ")
    print(tmp)



    instr = tmp[0].split(" ")
    # instr = ["".join(sorted(i)) for i in instr]
    print(instr)

    from collections import defaultdict
    c_m = {}
    s_m = {}
    todo = defaultdict(list)

    for j in sorted(instr, key=len):
        print(len(j), j)

        if len(j) == 2:
            print("this is 1")
            c_m[1] = j

        elif len(j) == 3:
            print("this is 7")
            c_m[7] = j

        elif len(j) == 4:
            print("this is 4")
            c_m[4] = j

        elif len(j) == 7:
            print("this is 8")
            c_m[8] = j

        else:
            todo[len(j)].append(j)

    print("c_m", c_m)

    print("todo", todo)
    s_m["a"] = [i for i in c_m[7] if not is_sub(c_m[1], i)][0]
    print("s_m", s_m)

    c_m[9] = [i for i in todo[6] if is_sub(i, c_m[1])][0]
    print("c_m", c_m)
    todo[6].remove(c_m[9])

    print(todo[5], c_m[1])
    c_m[3] = [i for i in todo[5] if is_sub(i,c_m[1])][0]
    print("c_m", c_m)
    todo[5].remove(c_m[3])

    c_m[0] = [i for i in todo[6] if is_sub(i,c_m[1])][0]
    print("c_m", c_m)
    todo[6].remove(c_m[0])

    c_m[6] = todo[6][0]
    print("c_m", c_m)

    s_m["d"] = [i for i in c_m[9] if is_sub(c_m[3], i)][0]
    print("s_m", s_m)

    c_m[2] = [i for i in todo[5] if is_sub(i, s_m["d"])][0]
    todo[5].remove(c_m[2])
    print("c_m", c_m)

    c_m[5] = todo[5][0]

    print("c_m", c_m)

    expr = tmp[1].split(" ")
    expr = ["".join(sorted(i)) for i in expr]
    print(expr)

    n_d = {"".join(sorted(v)):k for k,v in c_m.items()}

    t = [n_d[i] for i in expr]
    print(t)
    t = [i for i in t if i in [1,4, 7, 8]]
    c += len(t)

print(c)