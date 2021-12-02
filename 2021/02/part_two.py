file = open("input.txt", "r")
raw_input = list()

[raw_input.append(i[:-1]) for i in file.readlines()]

a = 0
h = 0
d = 0

for elem in raw_input:
    print(elem)
    t = elem.split(" ")
    print(t)
    if t[0] == "forward":
        h += int(t[1])
        d += int(t[1]) * a
    elif t[0] == "down":
        a += int(t[1])
    elif t[0] == "up":
        a -= int(t[1])

print(h, d, h*d)