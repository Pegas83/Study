a = []
b = []
c = []
for i in range(1, 13, 1):
    if i <= 4:
        a.append([i])
    if (i > 4) and (i <= 8):
        b.append([i])
    if i > 8:
        c.append([i])
d = [a, b, c]
for row in d:
    for column in row:
        print(column, end=' ')
    print()