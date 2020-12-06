with open("6_custom_customs_input.txt") as f:
    groups = f.read()

groups = groups.split("\n\n")

answers_sum = 0

groups[-1] = groups[-1].removesuffix("\n")  # remove the trailing newline from the last entry

for group in groups:
    group_answers = {}
    for person in group:
        for answer in person:
            if answer in group_answers:
                group_answers[answer] += 1
            else:
                group_answers[answer] = 1

    for answer_count in group_answers.values():
        if answer_count >= len(group.split("\n")):
            answers_sum += 1

print(answers_sum)
