
raw_input = [[int(j) for j in list(i[:-1])] for i in open("input.txt").readlines()]

s = 0

for i_s, row in enumerate(raw_input):
    print(row)

    # print(len(row))
    for i,v in enumerate(row):
        # print(i,v)
        # if i -1 >= 0:
        #     print("l")
        #     if not (v < row[i-1]):
        #         continue
        #
        # if i+1 < len(row):
        #     print("r")
        #     if not (v < row[i+1]):
        #         continue
        #
        # print(v)
        # print(row[i-1], v, row[i + 1])
        if (v < row[i-1] if i-1 >= 0 else True) and (v < row[i+1] if i+1 < len(row) else True):
            # print(v)
            if (v < raw_input[i_s -1][i] if i_s - 1 >= 0 else True) and (v < raw_input[i_s+1][i] if i_s+1 < len(raw_input) else True):
                print(v)
                print()

                s+= v+1

print(s)
