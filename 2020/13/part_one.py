if __name__ == '__main__':
    raw_input = [line[:-1] for line in open("input.txt").readlines()]
    # [print(i) for i in raw_input]

    current_time = int(raw_input[0])
    print(current_time)
    buses = [int(i) for i in raw_input[1].split(",") if i != "x"]

    print(buses)

    match = (int(current_time / buses[0]) + 1) * buses[0]
    print(match)
    match_bus_id = buses[0]

    for bus_id in buses[1:]:

        t = int(current_time / bus_id)

        lower = t * bus_id
        upper = (t + 1) * bus_id

        print(lower, upper)

        if match > upper:
            match = upper
            match_bus_id = bus_id

    print((match - current_time) * match_bus_id)
