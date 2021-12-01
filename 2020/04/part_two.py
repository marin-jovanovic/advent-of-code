import re

regex_map = {
        "byr": r"^19[2-9][0-9]|200[0-2]$",
        "iyr": r"^201[0-9]|2020$",
        "eyr": r"^202[0-9]|2030$",
        "hgt": r"^(1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in$",
        "hcl": r"^#[0-9,a-f]{6}$",
        "ecl": r"^amb|blu|brn|gry|grn|hzl|oth$",
        "pid": r"^\d{9}$"
        }

raw_lines = open("input.txt").read().split("\n\n")

lines = [dict(re.findall(r"([a-z]+):([\S]+)", i)) for i in raw_lines]

num_of_valid_passports = 0
for line in lines:
    if all(re.match(regex_map[i], line.get(i) or "") for i in regex_map):
        num_of_valid_passports += 1

print(num_of_valid_passports)
