filename = "input.txt"

from collections import defaultdict
mc = defaultdict(int)
l = 0

for line in open(filename, "r").readlines():
    line = line[:-1]
    l += 1
    t = list(line)
    print(t)

    for i, v in enumerate(t):
        mc[i] += int(v)

    print(line)

print(mc, l)

t = []
for k,v in mc.items():
    print(k, v)

    if v > l/2:
        print(1)
        t.append('1')
    else:
        print(0)
        t.append('0')

v = "".join(t)
s_v = v
print(v)
v = int(v,2)


print("f", v)

a = v

print(s_v)
n_v = []
for i in s_v:
    if i == "0":
        n_v.append("1")
    else:
        n_v.append("0")

v = "".join(n_v)
s_v = v
print(v)
v = int(v,2)


print("f", v)

print(a * v)