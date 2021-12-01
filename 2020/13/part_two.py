raw_input = [line[:-1] for line in open("input.txt").readlines()]
raw_input = raw_input[1]

buses = [int(i) if i != "x" else i for i in raw_input.split(",")]

# dict of offsets
t = {buses[0]: 0}
for i, bus in enumerate(buses[1:], start=1):
    if bus != "x":
        t[bus] = bus - i
print(t)

for k, v in t.items():
    while t[k] < 0:
        t[k] = t[k] + k

print(t)

# t = {2: 0, 3: 0, 24: 0, 6: 0, 7: 0}

t = dict(sorted(t.items(), key=lambda item: item[1], reverse=True))

print(t)

iterator = list(t.keys())[0]
increment = 1
for k, v in t.items():
    while iterator % k != v:
        iterator += increment
    increment *= k

print(iterator)
