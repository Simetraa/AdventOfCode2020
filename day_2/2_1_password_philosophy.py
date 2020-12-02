import re

with open("2_password_philosophy_input.txt") as f:
    database = f.read()

database = database.split("\n")
del database[-1]  # remove new line

# https://regexr.com/5hgso
extractor = re.compile("([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)")
valid_passwords = []

for record in database:
    groups = re.findall(extractor, record)

    min_ = int(groups[0][0])
    max_ = int(groups[0][1])
    char = groups[0][2]
    password = groups[0][3]

    if min_ <= password.count(char) <= max_:
        valid_passwords.append(record)

print(len(valid_passwords))