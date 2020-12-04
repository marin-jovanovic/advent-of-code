file = open("input.txt", "r")
raw_input = list()

[raw_input.append(i[:-1]) for i in file.readlines()]

counter = 0

for elem in raw_input:
    raw_tokens = elem.split(" ")

    lower_bound = int((raw_tokens[0].split("-")[0]))
    upper_bound = int((raw_tokens[0].split("-")[1]))
    letter = (raw_tokens[1])[:-1]

    counter += 1 if lower_bound <= raw_tokens[2].count(letter) <= upper_bound else 0

print(counter)
