import re

with open("4_passport_processing_input.txt") as f:
    records = f.read()

records = records.split("\n\n")

# https://regexr.com/5hn50
extractor = re.compile("([a-z]{3}):([\w\d#]+|\n)")
# https://regexr.com/5hnfj
hex_validator = re.compile("#[0-9a-f]{6}")

passports = []
for record in records:
    passports.append(dict(re.findall(extractor, record)))

required_fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")

valid_passports = []

for passport in passports:
    if not all(field in passport.keys() for field in required_fields):
        continue
    invalid_year = False
    for field in ("byr", "iyr", "eyr"):
        if len(passport[field]) != 4:
            invalid_year = True
    if invalid_year:
        continue
    if not 1920 <= int(passport["byr"]) <= 2002:
        continue
    if not 2010 <= int(passport["iyr"]) <= 2020:
        continue
    if not 2020 <= int(passport["eyr"]) <= 2030:  # cast these as well.
        continue

    if not re.search(hex_validator, passport["hcl"]):
        continue

    if passport["ecl"] not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
        continue

    if not passport["pid"].isdigit():
        continue
    if not len(passport["pid"]) == 9:
        continue

    if not passport["hgt"].endswith(("cm", "in")):
        continue
    if passport["hgt"].endswith("cm"):
        if not 150 <= int(passport["hgt"][:-2]) <= 193:
            continue
    if passport["hgt"].endswith("in"):
        if not 59 <= int(passport["hgt"][:-2]) <= 76:
            continue
    if not passport["hgt"].endswith(("cm", "in")):
        continue

    valid_passports.append(passport)

print("Valid passports:", len(valid_passports))