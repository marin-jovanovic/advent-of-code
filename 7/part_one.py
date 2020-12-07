
# if __name__ == '__main__':
#     #1 redak: Ulazni nizovi odvojeni znakom |. Simboli svakog pojedinog niza odvojeni su zarezom.
#     #  2. redak: Leksikografski poredan skup stanja odvojenih zarezom.
#     #  3. redak: Leksikografski poredan skup simbola abecede odvojenih zarezom.
#     #  4. redak: Leksikografski poredan skup prihvatljivih stanja odvojenih zarezom.
#     #  5. redak: Početno stanje.
#     #  6. redak i svi ostali retci: Funkcija prijelaza u formatu
#
#     # t_in = list()
#     # t_in.append("a,pnp,a|pnp,lab2|pnp,a|pnp,lab2,utr,utr")
#     # t_in.append("p5,s3,s4,st6,stanje1,stanje2")
#     # t_in.append("a,lab2,pnp,utr") # prihvatljivo
#     # t_in.append("p5") # pocetno
#     # t_in.append("stanje1")
#     # t_in.append("s3,a->stanje2")
#     # t_in.append("s3,lab2->p5,s4")
#     # t_in.append("s4,$->st6")
#     # t_in.append("s4,utr->p5,s3")
#     # t_in.append("stanje1,a->stanje2")
#     # t_in.append("stanje1,pnp->s3")
#     # t_in.append("stanje2,$->st6")
#     # t_in.append("stanje2,a->#")
#     #
#     # driver(t_in)
#
#     get_input()
#
#     for input_list in constants.INPUT_LISTS:
#         print(get_paths(input_list))

import re

source = "input.txt"

key = [(line.split("bags contain "))[0] for line in (open(source).read().split("\n"))[:-1]]
for line in key:
    print(line)
print()

key2 = [(((line.split("bags contain "))[0])[:-1] + ",") for line in (open(source).read().split("\n"))[:-1]]
for line in key2:
    print(line)
print()

value = [([value for value in line if value != "gs" and value != "g"]) for line in [re.split(" ba(g|gs), ",
    line) for line in [re.sub("[1-9]+ ", "", line) for line in [re.sub(" ba(g|gs)[.]", "",(line.split("contain "))[1]
    ) for line in (open(source).read().split("\n"))[:-1]]]]]
for line in value:
    print(line)
print()



counter = 0

for k in key:
    r = list()
    r.append("a,a") #1
    # all bags
    r.append(("".join(key2))[:-1])
    r.append("a")
    # target bag
    r.append("shiny gold")
    # initial bag
    r.append(k[:-1])
    # transitions

    for i in range(len(key)):
        for j in value[i]:
            if j == "no other":
                continue

            t = str(key[i])[:-1] + ",$->" + str(j)
            r.append(t)

    f = open("temp.txt", "a")
    for line in r:
        f.write(line + "\n")
    f.close()

    import os
    program_output_lines = \
        (os.popen("py C:\\git\\advent-of-code-2020\\7\\nfa\\main.py < \"C:\\git\\advent-of-code-2020\\7\\temp.txt\"").read().split("\n"))[0]

    c = k[:-1] + "->" + program_output_lines.replace("," , "->")

    if "shiny gold" in c and not c.startswith("shiny gold"):
        print(c)
        counter += 1

    f = open("temp.txt", "w")
    f.close()

print(counter)

