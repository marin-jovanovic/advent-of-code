formatted_lines = sorted([int(line[:-4].replace("F", "0").replace("B", "1"), 2) * 8 +
                   int(line[7:-1].replace("L", "0").replace("R", "1"), 2)
                   for line in open("input.txt").readlines()])
print(formatted_lines)

for i in range(len(formatted_lines) - 1):
    if formatted_lines[i] + 1 != formatted_lines[i+1]:
        print(formatted_lines[i] + 1)
