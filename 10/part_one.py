lines = sorted(map(int, open("input.txt", "r").read().strip().splitlines()))

lines = [0] + lines + [lines[-1] + 3]
print(lines)

c1 = c3 = 0

for i, element in enumerate(lines):
    try:
        if element + 1 == lines[i+1]:
            c1 += 1
        elif element + 3 == lines[i+1]:
            c3 += 1
    except:
        print(c1 * c3)
