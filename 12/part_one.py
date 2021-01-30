def log(*data):
    print(data)


lines = [line[:-1] for line in open("input.txt").readlines()]

course = "E"

n = 0
e = 0

for line in lines:
    log(n, e, course)
    log()
    log(line)

    nav = line[:1]
    units = int(line[1:])

    if nav == "F":
        if course == "N":
            n += units
        elif course == "E":
            e += units
        elif course == "W":
            e -= units
        elif course == "S":
            n -= units

    elif nav == "R":
        if units == 90:
            if course == "E":
                course = "S"
            elif course == "S":
                course = "W"
            elif course == "W":
                course = "N"
            else:
                course = "E"

        elif units == 180:
            if course == "E":
                course = "W"
            elif course == "S":
                course = "N"
            elif course == "W":
                course = "E"
            else:
                course = "S"

        elif units == 270:
            if course == "E":
                course = "N"
            elif course == "S":
                course = "E"
            elif course == "W":
                course = "S"
            else:
                course = "W"

    elif nav == "L":
        if units == 270:
            if course == "E":
                course = "S"
            elif course == "S":
                course = "W"
            elif course == "W":
                course = "N"
            else:
                course = "E"

        elif units == 180:
            if course == "E":
                course = "W"
            elif course == "S":
                course = "N"
            elif course == "W":
                course = "E"
            else:
                course = "S"

        elif units == 90:
            if course == "E":
                course = "N"
            elif course == "S":
                course = "E"
            elif course == "W":
                course = "S"
            else:
                course = "W"

    elif nav == "N":
        n += units

    elif nav == "E":
        e += units

    elif nav == "W":
        e -= units

    else:
        n -= units

log(n, e, course)
log()


print("n", n)
print("e", e)
print(abs(n) + abs(e))