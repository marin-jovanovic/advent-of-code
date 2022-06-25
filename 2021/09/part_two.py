
raw_input = [[int(j) for j in list(i[:-1])] for i in open("input.txt").readlines()]

s = 0

for i,v in enumerate(raw_input):
    print(i,v)
print()

to_check = []

sums = []

for i_s, row in enumerate(raw_input):
    print(row)

    for i,v in enumerate(row):

        if (v < row[i-1] if i-1 >= 0 else True) and (v < row[i+1] if i+1 < len(row) else True):
            if (v < raw_input[i_s -1][i] if i_s - 1 >= 0 else True) and (v < raw_input[i_s+1][i] if i_s+1 < len(raw_input) else True):

                print(v)
                print(i_s, i)

                to_check = []
                checked = []
                checked.append((i, i_s))

                if  i_s -1 >= 0 :
                    if not (raw_input[i_s-1][i] == 9):
                        to_check.append((i, i_s - 1))

                if  i_s +1 < len(raw_input) :
                    if not (raw_input[i_s+1][i] == 9):
                        to_check.append((i, i_s+1))

                if i-1 >= 0 :
                    if not (raw_input[i_s][i-1] == 9):
                        to_check.append((i-1, i_s))

                if i+1 < len(row):
                    if not (raw_input[i_s][i+1] == 9):
                        to_check.append((i+1, i_s))

                print("to check", to_check)
                print("checked", checked)
                print()

                while to_check:

                    to_check_new = []

                    for j in to_check:
                        print(j)
                        checked.append(j)

                        c_i = j[0]
                        c_i_s = j[1]

                        if  c_i_s -1 >= 0 :
                            if not (raw_input[c_i_s-1][c_i] == 9):
                                if (c_i, c_i_s-1) not in checked:
                                    to_check_new.append((c_i, c_i_s - 1))

                        if  c_i_s +1 < len(raw_input) :
                            if not (raw_input[c_i_s+1][c_i] == 9):
                                if (c_i, c_i_s+1) not in checked:

                                    to_check_new.append((c_i, c_i_s+1))

                        if c_i-1 >= 0 :
                            if not (raw_input[c_i_s][c_i-1] == 9):
                                if (c_i-1, c_i_s) not in checked:

                                    to_check_new.append((c_i-1, c_i_s))

                        if c_i+1 < len(row):
                            if not (raw_input[c_i_s][c_i+1] == 9):
                                if (c_i+1, c_i_s) not in checked:

                                    to_check_new.append((c_i+1, c_i_s))

                    print("to chekc new ", to_check_new)

                    to_check = to_check_new

                print("cheched", checked)
                sums.append(len(set(checked)))
                print("-----------------------------------")

print(sums)


def multiplyList(myList):
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result

s = sorted(sums)[-3:]
print(s)

r = multiplyList(s)
print(r)