print('Enter the amount of rows')
rows = int(input())
print('Enter the amount of columns')
columns = int(input())
last = 1
change = []
matrix = []
for i in range(rows):
#        matrix = []
        row = []
        for j in range(columns):
            row.append(last)
            last = last + 1
        if i % 2 != 0:
            for k in range(len(row)-1, -1, -1):
                change.append(row[k])
            matrix.append(change)
        if i % 2 == 0:
            matrix.append(row)
for string in matrix:
    for column in string:
        print(column, end=' ')
    print()

