print('Введите 3 одинаковых числа и одно отличное')
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
if num1 != num2 and num1 != num3 and num1 != num4:
    print('Порядковый номер отличного числа - 1')
elif num2 != num1 and num2 != num3 and num2 != num4:
    print('Порядковый номер отличного числа - 2')
elif num3 != num1 and num3 != num2 and num3 != num4:
    print('Порядковый номер отличного числа - 3')
else:
    print('Порядковый номер отличного числа - 4')