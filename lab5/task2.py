rows = 6
cols = 6

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        value = 7 - abs(i - j)
        row.append(value)
    matrix.append(row)

for row in matrix:
    print(" ".join(map(str, row)))
