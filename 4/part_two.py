import re
file = open("input.txt", "r")
lines = list()

[lines.append(i[:-1]) for i in file.readlines()]

passport_data = list()

num_of_valid_passports = 0


def all_in(candidates, sequence):
    for element in candidates:
        if element not in sequence:
            return False
    return True


def check():
    global num_of_valid_passports



    for element in passport_data:
        raw_data = element.split(":")

        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        if raw_data[0] == "byr":
            try:
                if not (1920 <= int(raw_data[1]) <= 2002):
                    return False
                else:
                    print("byr ok")
            except:
                return False

        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        elif raw_data[0] == "iyr":
            try:

                if not (2010 <= int(raw_data[1]) <= 2020):
                    return False
                else:
                    print("iyr ok")
            except:
                return False

        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        elif raw_data[0] == "eyr":

            try:

                if not (2020 <= int(raw_data[1]) <= 2030):
                    return False
                else:
                    print("eyr ok")

            except:
                return False

        # hgt (Height) - a number followed by either cm or in:
        # If cm, the number must be at least 150 and at most 193.
        # If in, the number must be at least 59 and at most 76.
        elif raw_data[0] == "hgt":

            try:

                if re.match("[1]\d\d[c][m]", raw_data[1]):
                    data = raw_data[1].replace("cm", "")
                    if not (150 <= int(data) <= 193):
                        return False
                    else:
                        print("hgt cm ok")

                elif re.match("\d{2}[i][n]", raw_data[1]):
                    data = raw_data[1].replace("in", "")
                    if 59 <= int(data) <= 76:
                        print("hgt in ok")
                    else:
                        return False
                else:
                    return False

            except:
                return False

        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        elif raw_data[0] == "hcl":
            if not re.match("[#](\d|[a-f]){6}", raw_data[1]):
                return False
            else:
                print("hcl ok")

        # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        elif raw_data[0] == "ecl":
            if not (raw_data[1] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
                return False
            else:
                print("ecl ok")

        # pid (Passport ID) - a nine-digit number, including leading zeroes.
        elif raw_data[0] == "pid":
            if not re.match("\d{9}", raw_data[1]):
                return False
            else:
                print("pid ok")

        # cid (Country ID) - ignored, missing or not.
        elif raw_data[0] == "cid":
            print("cid ok")

        else:
            return False

    num_of_valid_passports += 1


def areAllFieldsPresent():

    elem = list()
    for e in passport_data:
        k = e.split(":")
        elem.append(k[0])


    return all_in(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"], elem)


for line in lines:

    if(line == ""):
        passport_data.sort()
        print(passport_data)

        if areAllFieldsPresent():
            print("ok")
            if not check():
                print("not ok")

        passport_data.clear()

    else:
        raw_data = line.split(" ")
        for raw_element in raw_data:
            if raw_element.startswith("cid"):
                continue
            # tag = (raw_element.split(":"))[0]
            passport_data.append(raw_element)

passport_data.sort()
print(passport_data)

if areAllFieldsPresent():
    print("ok")
    check()

print(num_of_valid_passports)


# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)          optional
# 148 lower