lines = [int(line[:-1]) for line in open("input.txt").readlines()]

[print(line) for line in lines]

target = 177777905

print("")

for i in range(len(lines)):
    r = int(lines[i])
    print(r)
    min = max = r

    for j in range(i + 1, len(lines)):

        c = lines[j]

        print("\t" + str(c))
        r += c

        if min > c:
            min = c
        elif max < c:
            max = c

        if r > target:
            break
        elif r == target:
            print("\nmatch")

            print(min, max)
            print(min + max)
            import sys
            sys.exit()
