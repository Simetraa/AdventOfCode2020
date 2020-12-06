import string

with open("6_custom_customs_input.txt") as f:
    groups = f.read()

groups = groups.split("\n\n")


answers_sum = 0

for group in groups:
    answers = {}
    persons = group.split("\n")
    for person in persons:
        for answer in person:
            answers[answer] = True
    answers_sum += sum(answers.values())

print(answers_sum)
