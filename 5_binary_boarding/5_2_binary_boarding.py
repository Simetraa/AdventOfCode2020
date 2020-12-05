with open("5_binary_boarding_input.txt") as f:
    passes = f.read()

passes = passes.split("\n")
del passes[-1]  # remove new line

scanned_seat_ids = []

rows = 8
cols = 128


for pass_code in passes:
    row = pass_code[:7]
    col = pass_code[-3:]

    row = row.replace("F", "0")
    row = row.replace("B", "1")
    row = int(row, 2)  # convert to int base 2

    col = col.replace("L", "0")
    col = col.replace("R", "1")
    col = int(col, 2)

    seat_id = row * 8 + col
    scanned_seat_ids.append(seat_id)


for seat_id in range(max(scanned_seat_ids)):
    if seat_id in scanned_seat_ids:
        continue
    if seat_id+1 in scanned_seat_ids:
        if seat_id-1 in scanned_seat_ids:
            print(seat_id)
