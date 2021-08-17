print('Enter a number consisting of an even number of digits')
num = int(input())
check_num = num
dig = 0
sum = 0
'''Что значит Shadows built-in name 'sum' ?'''
while check_num > 0:
    check_num = check_num // 10
    dig = dig + 1
check_dig = dig
while check_dig > 0:
    if check_dig > dig/2:
        sum = sum + num % 10
    if check_dig > 0:
        sum = sum - num % 10
    num = num // 10
    check_dig = check_dig - 1
if sum == 0:
    print('The sums of the first half and the second half of digits are equal')
else:
    print('The sums of the first half and the second half of digits are unequal')
