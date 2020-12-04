file = open("input.txt", "r")
raw_input = list()

[raw_input.append(i[:-1]) for i in file.readlines()]

counter = 0

for elem in raw_input:
    raw_tokens = elem.split(" ")

    lower_bound = int((raw_tokens[0].split("-")[0]))
    upper_bound = int((raw_tokens[0].split("-")[1]))
    letter = (raw_tokens[1])[:-1]

    print(elem)

    a = (raw_tokens[2])[lower_bound - 1]
    b = (raw_tokens[2])[upper_bound - 1]

    if (a == letter) != (b == letter):
        counter += 1

print(counter)

