print('Задайте начальную координату x функции y=x2+x')
x = float(input())
print('Задайте шаг увеличения координаты х')
step = float(input())
print('Задайте конечную координату х')
end = float(input())
print(' x  |   y   |   y!')
while x <= end:
    y = x**2+x
    if y-y//1 != 0 and y != 0:
        print(x, '|', y, '| у-дробное число. Вычисление факториала прервано')
    else:
        fact = 1
        i = 1
        while i <= y:
            fact = fact * i
            i = i + 1
        print(x, '|', y, '|', fact)
    x = x + step


