import re

source = "input.txt"

for line in open(source).readlines():
    print(line[:-1])
print()

start = ""
key = list()
value = list()

for i in open(source).readlines():
    i = i[:-1]
    i = i.replace("bags.", "").replace("bag.", "").replace("bags", "").replace("bag", "")

    if i.startswith("shiny gold"):
        start = i.replace("shiny gold  contain ", "").replace(" , ", " + ")
        continue
    elif i.endswith("  contain no other "):
        i = i.replace("  contain no other ", " = 1 ")

    i = i[:-1].replace(" contain", "=").replace(" , ", " + ")
    raw_data = i.split(" = ")
    print(raw_data)
    key.append(raw_data)
print()

print(start)
print()

while re.search("[a-z]", start) is not None:
    for elem in key:

        if start.__contains__(elem[0]):
            c = str(re.findall("[0-9]+ " + elem[0], start)[0]).replace(" " + elem[0], "")

            if elem[1] == "1":
                start = start.replace(elem[0], "* (" + elem[1] + ")", 1)
            else:
                start = start.replace(elem[0], "* (" + elem[1] + ") + " + str(c), 1)
            print(start)

print(start)
print(eval(start))
