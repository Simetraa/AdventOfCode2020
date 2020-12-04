import re

with open("4_passport_processing_input.txt") as f:
    records = f.read()

records = records.split("\n\n")

# https://regexr.com/5hn50
extractor = re.compile("([a-z]{3}):([\w\d#]+|\n)")

passports = []
for record in records:
    passports.append(dict(re.findall(extractor, record)))

required_fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")

valid_passports = []

for passport in passports:
    if all(field in passport.keys() for field in required_fields):
        valid_passports.append(passport)

print("Valid passports:", len(valid_passports))
