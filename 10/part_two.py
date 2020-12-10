lines = sorted(map(int, open("input.txt", "r").read().strip().splitlines()))

lines = [0] + lines + [lines[-1] + 3]
print(lines)

# x = index
# (i, j)  = tuple of current and next elem
start_index_list = [x for x, (i, j) in enumerate(zip(lines[:-1], lines[1:])) if i + 3 == j]
print(start_index_list)


result = 1
i = -1
for j in start_index_list:
    result *= (2 ** max(1, j - i - 2)) - int(lines[j] - lines[i + 1] != 3 and j - i != 3)
    i = j

print(result)