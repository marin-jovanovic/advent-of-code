# lines = [line[:-1] for line in open("input.txt").readlines()]
# # print(lines)
#
# c = 0
#
# def is_sub(big, small):
#     return all(x in big for x in small)
#
# for i in lines:
#     tmp = i.split(" | ")
#     # print(tmp)
#
#     instr = tmp[0].split(" ")
#
#     from collections import defaultdict
#     c_m = {}
#     s_m = {}
#     todo = defaultdict(list)
#
#     for j in sorted(instr, key=len):
#         # print(j)
#
#         if len(j) == 2:
#             c_m[1] = j
#
#         elif len(j) == 3:
#             c_m[7] = j
#
#         elif len(j) == 4:
#             c_m[4] = j
#
#         elif len(j) == 7:
#             c_m[8] = j
#
#         else:
#             todo[len(j)].append(j)
#
#     # print(c_m)
#     # print(todo)
#
#     c_m[6] = [i for i in todo[6] if not is_sub(i, c_m[1])][0]
#     todo[6].remove(c_m[6])
#     # print(c_m)
#     # print(todo)
#
#     c_m[9] = [i for i in todo[6] if is_sub(i, c_m[4])][0]
#     todo[6].remove(c_m[9])
#
#     c_m[0] = todo[6][0]
#
#     c_m[3] = [i for i in todo[5] if is_sub(i,c_m[1])][0]
#     todo[5].remove(c_m[3])
#
#     two_t = [i for i in c_m[4] if is_sub(c_m[7], i)][0]
#
#     c_m[5] = [i for i in todo[5] if is_sub(i, two_t)][0]
#     todo[5].remove(c_m[5])
#
#     c_m[2] = todo[5][0]
#
#     expr = tmp[1].split(" ")
#     expr = ["".join(sorted(i)) for i in expr]
#
#     n_d = {"".join(sorted(v)):k for k,v in c_m.items()}
#
#     t = "".join([str(n_d[i]) for i in expr])
#     print(t)
#     print()
#     c += int(t)
#
# print(c)

# raw_input = [i[:-1].split(" | ") for i in open("in.txt").readlines()]
#
# s = 0
#
#
#
#
# for row in raw_input:
#     # print(row)
#
#     decoded = {}
#
#     todo = sorted(row[0].split(" "), key=len)
#
#     for number in todo:
#
#         print(len(number))
#
#
#         decoded[
#             {
#                 2:1,
#                 3:7,
#                 4:4
#
#             }
#             [len(number)]] = number
#
#
#
#         t = {
#             2: 1,
#             3: 7,
#             4: 4,
#             5: 3 if set(decoded[1]).issubset(set(number)) else
#             (5 if set(number).issubset(set(decoded[9])) else 2),
#             6 : 9 if set(decoded[4]).issubset(set(number)) else
#             (6 if not set(decoded[1]).issubset(set(number)) else (
#                 0 if set(decoded[4]).issubset(set(number)) and set(decoded[1]).issubset(set(number)) else -1
#             )),
#             7:8
#         }
#
#         decoded[t[len(number)]] = number
#
#
#
#         # if len(number) == 2:
#         #     decoded[1] = number
#         #
#         # elif len(number) == 3:
#         #     decoded[7] = number
#         #
#         # elif len(number) == 4:
#         #     decoded[4] = number
#         #
#         # elif len(number) == 6 and set(decoded[4]).issubset(set(number)):
#         #     decoded[9] = number
#         #
#         # elif len(number) == 6 and not set(decoded[1]).issubset(set(number)):
#         #     decoded[6] = number
#         #
#         # elif len(number) == 6 and not set(decoded[4]).issubset(set(number)) and set(decoded[1]).issubset(set(number)):
#         #     decoded[0] = number
#         #
#         # elif len(number) == 7:
#         #     decoded[8] = number
#
#     for number in todo:
#
#         if  len(number) == 5 and set(decoded[1]).issubset(set(number)):
#             decoded[3] = number
#
#         elif  len(number) == 5 and set(number).issubset(set(decoded[9])):
#             decoded[5] = number
#
#         elif len(number) == 5 and not set(number).issubset(set(decoded[9])):
#             decoded[2] = number
#
#     formatted = {"".join(sorted(v)): k for k,v in decoded.items()}
#
#     t = ""
#     for i in ["".join(sorted(i)) for i in row[1].split(" ")]:
#         t += str(formatted[i])
#
#     print(t)
#     print()
#
#     s += int(t)
#
# print(s)

raw_input = [i[:-1].split(" | ") for i in open("input.txt").readlines()]

s = 0

for row in raw_input:
    # print(row)

    decoded = {}

    todo = sorted(row[0].split(" "), key=len)
    remove = []

    for number in todo:

        if len(number) == 2:
            decoded[1] = number

        elif len(number) == 3:
            decoded[7] = number

        elif len(number) == 4:
            decoded[4] = number

        elif len(number) == 6 and set(decoded[4]).issubset(set(number)):
            decoded[9] = number

        elif len(number) == 6 and not set(decoded[1]).issubset(set(number)):
            decoded[6] = number

        elif len(number) == 6 and not set(decoded[4]).issubset(set(number)) and set(decoded[1]).issubset(set(number)):
            decoded[0] = number

        elif len(number) == 7:
            decoded[8] = number

    for number in todo:
        if  len(number) == 5 and set(decoded[1]).issubset(set(number)):
            decoded[3] = number

        elif  len(number) == 5 and set(number).issubset(set(decoded[9])):
            decoded[5] = number

        elif len(number) == 5 and not set(number).issubset(set(decoded[9])):
            decoded[2] = number

    formatted = {"".join(sorted(v)): k for k,v in decoded.items()}

    t = ""
    for i in ["".join(sorted(i)) for i in row[1].split(" ")]:
        t += str(formatted[i])

    print(t)
    print()

    s += int(t)

print(s)