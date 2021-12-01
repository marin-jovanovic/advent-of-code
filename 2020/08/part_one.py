import re

acc = ""

lines = [line[:-1] for line in open("input.txt").readlines()]
print(lines)


def log(t):
    print("\t" + str(t))

i = -1
visited = list()
while True:
    i += 1
    log(visited)
    if visited.__contains__(i):
        print("--------")
        break
    visited.append(i)

    print(i, lines[i])

    r = (re.findall("[+|-][0-9]+", lines[i]))[0]
    log(r)

    if lines[i].startswith("jmp"):
        i += int(r) - 1
        log("i = " + str(i))
    elif lines[i].startswith("acc"):
        acc += r

print(acc)
print(eval(acc))
