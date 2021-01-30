filename = "input.txt"

lines = list()

right_jump = 1
down_jump = 2

down_buffer = 0
t = 0

num_of_trees = 0

for line in open(filename, "r").readlines():

    if down_buffer != 0:
        line = line[:-1].replace(".", "0").replace("#", "1")

        lines.append([int(i) for i in list(line)])

        down_buffer -= 1
        continue

    down_buffer = down_jump

    line = line[:-1].replace(".", "0").replace("#", "1")

    temp = [int(i) for i in list(line)]
    line = [i for i in list(temp)]

    try:
        line[t] = 3

    except:
        t %= len(line)
        line[t] = 3

    if temp[t] == 1:
        num_of_trees += 1

    t += right_jump

    lines.append([i for i in list(line)])

    down_buffer -= 1

print(num_of_trees)

print(78 * 247 * 68 * 69 * 33)
# Right 1, down 1. -> 78
# Right 3, down 1. -> 247
# Right 5, down 1. -> 68
# Right 7, down 1. -> 69
# Right 1, down 2. -> 33
