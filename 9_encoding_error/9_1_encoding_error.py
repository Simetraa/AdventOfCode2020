with open("9_encoding_error_input.txt") as f:
    data = f.readlines()

data = [int(datum) for datum in data]

del data[-1]  # remove new line

PREAMBLE_LENGTH = 25

for index in range(PREAMBLE_LENGTH, len(data)):
    preamble = data[index-PREAMBLE_LENGTH:index]
    found = False
    for item in preamble:
        for item2 in preamble:
            if item + item2 == data[index] and item != item2:
                found = True
                break
        if found:
            break
    if not found:
        invalid_number = data[index]

print(invalid_number)

