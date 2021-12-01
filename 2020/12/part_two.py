def log(*data):
    print(data)


if __name__ == '__main__':
    lines = [line[:-1] for line in open("input.txt").readlines()]

    [print(line) for line in lines]
    print()
    initN = 1
    initE = 10

    waypoint = [initN, initE]
    ship = [0, 0]

    for line in lines:
        action = line[:1]
        value = int(line[1:])

        if action == "N":
            waypoint[0] += value

        elif action == "S":
            waypoint[0] -= value

        elif action == "E":
            waypoint[1] += value

        elif action == "W":
            waypoint[1] -= value

        elif action == "L":

            if value == 90:
                n = waypoint[0]
                e = waypoint[1]

                waypoint[0] = e
                waypoint[1] = -n

            elif value == 180:
                waypoint[0] = -waypoint[0]
                waypoint[1] = -waypoint[1]

            elif value == 270:
                n = waypoint[0]
                e = waypoint[1]

                waypoint[0] = -e
                waypoint[1] = n

            else:
                print("TODO")
                print(line)
                import sys
                sys.exit()

        elif action == "R":

            if value == 90:
                n = waypoint[0]
                e = waypoint[1]

                waypoint[0] = -e
                waypoint[1] = n

            elif value == 180:
                n = waypoint[0]
                e = waypoint[1]

                waypoint[0] = -waypoint[0]
                waypoint[1] = -waypoint[1]

            elif value == 270:
                n = waypoint[0]
                e = waypoint[1]

                waypoint[0] = e
                waypoint[1] = -n

            else:
                print("TODO")
                print(line)
                import sys
                sys.exit()

        elif action == "F":
            ship[0] += waypoint[0] * value
            ship[1] += waypoint[1] * value

        print("waypoint", waypoint)
        print("ship", ship)
        print()

    print(abs(ship[0]) + abs(ship[1]))
