file = open("input.txt", "r")
raw_input = list()

[raw_input.append(i[:-1]) for i in file.readlines()]

f = 0
d = 0

for elem in raw_input:
    print(elem)
    t = elem.split(" ")
    print(t)
    if t[0] == "forward":
        f += int(t[1])
    elif t[0] == "down":
        d += int(t[1])
    elif t[0] == "up":
        d -= int(t[1])

print(f, d)
print(f * d)