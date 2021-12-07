raw_input_lines = open("input.txt").read().split("\n")[:-1][0].split(",")
raw_input_lines = [int(i) for i in raw_input_lines]
print(raw_input_lines)

distances = []
g = lambda x: int(x*(x+1)/2)

print(min(
    [sum([g(abs(x-i)) for x in raw_input_lines])
     for i in range(min(raw_input_lines), max(raw_input_lines))
     ]
))
