raw_input_lines = open("input.txt").read().split("\n")
print(raw_input_lines)

formatted_lines = [int(line[:-4].replace("F", "0").replace("B", "1"), 2) * 8 +
                   int(line[7:-1].replace("L", "0").replace("R", "1"), 2)
                   for line in open("input.txt").readlines()]
print(formatted_lines)
print(max(formatted_lines))
