with open("9_encoding_error_input.txt") as f:
    data = f.readlines()

data = [int(datum) for datum in data]

del data[-1]  # remove new line

INVALID_NUMBER = 2089807806

found = False
for index in range(len(data)):
    for index2 in range(index, len(data)):

        if index2 > INVALID_NUMBER:
            break
        if sum(data[index:index2]) == INVALID_NUMBER:
            found = data[index:index2]
            break
    if found:
        break

print(min(found) + max(found))
