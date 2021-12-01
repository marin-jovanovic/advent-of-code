l = open("input.txt", "r").readlines()
print(len([1 for i, v in enumerate([(int(i[:-1])) for i in l]) if v > [(int(i[:-1])) for i in l][i-1]]))
