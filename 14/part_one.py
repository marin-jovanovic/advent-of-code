def dtb(data):
    return bin(data).replace("0b", "")


def driver():
    global d, raw_input
    mask = (raw_input[0].split(" = "))[1]

    raw_input = raw_input[1:]

    mem_locations = []

    try:
        while not str(raw_input[0]).startswith("mask"):
            line = raw_input[0]

            mem_locations.append(line[4:])

            raw_input = raw_input[1:]
    except:
        pass

    print(mask)
    [print(line) for line in mem_locations]
    print()

    rev_mask = mask[::-1]

    for line in mem_locations:
        t = line.split("] = ")
        location = t[0]

        d[location] = 36 * "0"

    [print(k, v) for k, v in d.items()]
    print()

    for line in mem_locations:
        t = line.split("] = ")
        print(t)
        location = t[0]
        val = dtb(int(t[1]))

        print("mem location: ", location)

        rev_val = str(val)[::-1]
        print("reversed mask:", rev_mask)

        while len(rev_val) != len(rev_mask):
            if len(rev_val) < len(rev_mask):
                break

            else:
                rev_mask += "X"

        print("reversed val: ", rev_val)

        prev = d[location]

        t = [i for i in prev]

        print("prev val:     ", prev)

        for num, i in enumerate(rev_mask):
            if i == "1":
                t[num] = i
            elif i == "0":
                t[num] = i

            elif i == "X":
                try:
                    t[num] = rev_val[num]
                except IndexError:
                    t[num] = "0"

        print("new val:      ", "".join(t))

        d[location] = "".join(t)

        print()

    [print(k, v) for k, v in d.items()]
    print()


if __name__ == '__main__':

    d = {}

    raw_input = [line[:-1] for line in open("input.txt").readlines()]
    [print(line) for line in raw_input]
    print()

    while raw_input:
        driver()

    sum = 0
    for k, v in d.items():
        print(k)
        print(v)
        t = v[::-1]
        print(t)

        t = int(t, 2)
        print(t)

        print()

        sum += t

    print(sum)
