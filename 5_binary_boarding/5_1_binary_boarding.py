with open("5_binary_boarding_input.txt") as f:
    passes = f.read()

passes = passes.split("\n")
del passes[-1]  # remove new line

scanned_seat_ids = []

for pass_ in passes:
    row = pass_[:7]
    col = pass_[-3:]

    row = row.replace("F", "0")
    row = row.replace("B", "1")
    row = int(row, 2)  # convert to int base 2

    col = col.replace("L", "0")
    col = col.replace("R", "1")
    col = int(col, 2)

    seat_id = row * 8 + col
    scanned_seat_ids.append(seat_id)

print(max(scanned_seat_ids))
