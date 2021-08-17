'''list = [1, 2, 3, 4, 45, 12, 9, 183, 66, 3, 2, 5, 55, 34, 101]
sum_chet = 0
sum_nechet = 0
for digit in list:
    if digit % 2 == 0:
        sum_chet = sum_chet + digit
    else:
        sum_nechet = sum_nechet + digit
print(sum_chet)
print(sum_nechet)'''
list = [1, 2, 3, 4, 45, 12, 9, 183, 66, 3, 2, 5, 55, 34, 101]
sum_chet = 0
poz = len(list)
for i in range(0, poz-1, 1):
    sum = list[i] + list[i+1]
    dif = list[i] - list[i+1]
    print(sum, dif)
