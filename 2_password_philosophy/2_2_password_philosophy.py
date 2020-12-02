import re

with open("2_password_philosophy_input.txt") as f:
    database = f.read()

database = database.split("\n")
del database[-1] # remove new line

extractor = re.compile("([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)")

valid_passwords = []
for record in database:
    groups = re.findall(extractor, record)

    pos1 = int(groups[0][0]) - 1  # index 1
    pos2 = int(groups[0][1]) - 1
    char = groups[0][2]
    password = groups[0][3]

    if len(password) >= pos2:
        if [password[pos1], password[pos2]].count(char) == 1:
            valid_passwords.append(password)


print(len(valid_passwords))