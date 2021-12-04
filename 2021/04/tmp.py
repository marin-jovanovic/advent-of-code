file = open("input.txt", "r")
lines = list()

[lines.append(i[:-1]) for i in file.readlines()]

f_l = [int(i) for i in lines[0].split(",")]
print(f_l)

print(sorted(f_l))

print(sorted(list(set(f_l))) == sorted(f_l))