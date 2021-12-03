filename = "input.txt"

lines = list()

num_of_rows = 0
right_jump = 3
down_jump = 2

prev_line_target = -1
down_buffer = 0
t = 0

for line in open(filename, "r").readlines():

    if down_buffer != 0:
        line = line[:-1].replace(".", "0").replace("#", "1")

        lines.append([int(i) for i in list(line)])

        down_buffer -= 1
        continue

    down_buffer = down_jump


    line = line[:-1].replace(".", "0").replace("#", "0")

    temp = list()
    temp = [int(i) for i in list(line)]
    line = temp

    try:
        line[t] = 3
        t += right_jump
    except:
        t = t % len(line)
        line[t] = 3
        t += right_jump

    lines.append([int(i) for i in list(line)])

    num_of_rows += 1

    down_buffer -= 1


for i in lines:
    print(i)


# print(sum(lines[i][num_of_rows-i-1] for i in range(num_of_rows)))















