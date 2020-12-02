with open("1_report_repair_input.txt") as f:
    expenses = f.read()

expenses = expenses.split()
expenses = [int(expense) for expense in expenses]

for expense1 in expenses:
    for expense2 in expenses:
        if expense1 + expense2 == 2020:
            print(expense1*expense2)
