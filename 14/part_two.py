def dtb(data):
    return bin(data).replace("0b", "")


if __name__ == '__main__':
    raw_input = [line[:-1] for line in open("input2.txt").readlines()]

    [print(i) for i in raw_input]
    print()

    while True:
        try:
            line = raw_input[0]
        except IndexError:
            break

        raw_input = raw_input[1:]
        # print(line)

        mask = (line.split(" = "))[1]
        print("mask:", mask)

        mem = []

        try:
            while not raw_input[0].startswith("mask = "):
                # print(raw_input[0])
                # t = raw_input[0]
                # t = (raw_input[0])[4:]
                # print(t)
                t = (((raw_input[0])[4:]).split("] = "))[0]
                # print(t)

                mem.append(dtb(int(t)))

                raw_input = raw_input[1:]

        except IndexError:
            pass

        [print(i) for i in mem]
        # print()

        mask_rev = mask[::-1]
        mem_rev = [i[::-1] for i in mem]

        print("mask_rev: ", mask_rev)

        print("mem_rev:", str(mem_rev))
        # [print(i) for i in mem_rev]
        print()

        print(dtb(100))