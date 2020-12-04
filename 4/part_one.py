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
    if all_in(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"], passport_data):
        num_of_valid_passports += 1


for line in lines:

    if(line == ""):

        print(passport_data)

        check()

        passport_data.clear()

    else:
        raw_data = line.split(" ")
        for raw_element in raw_data:
            tag = (raw_element.split(":"))[0]
            passport_data.append(tag)

print(passport_data)

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
