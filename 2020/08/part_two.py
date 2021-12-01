import re


def log(t):
    print("\t" + str(t))


def tester():
    acc = ""
    i = -1
    visited = list()

    try:
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

        print("error still present")

    except:
        print("no error")
        print(acc)
        print(eval(acc))
        import sys
        sys.exit()


lines = [line[:-1] for line in open("input.txt").readlines()]
print(lines)
print()

for instruction in range(len(lines)):
    print(lines[instruction])

    if lines[instruction].startswith("nop"):
        log("try this")
        r = (re.findall("[+|-][0-9]+", lines[instruction]))[0]
        log(r)
        print(lines)
        lines[instruction] = lines[instruction].replace("nop", "jmp")
        print(lines)
        tester()
        lines[instruction] = lines[instruction].replace("jmp", "nop")

    elif lines[instruction].startswith("jmp"):
        log("try this")
        r = (re.findall("[+|-][0-9]+", lines[instruction]))[0]
        log(r)
        print(lines)
        lines[instruction] = lines[instruction].replace("jmp", "nop")
        print(lines)
        tester()
        lines[instruction] = lines[instruction].replace("nop", "jmp")

