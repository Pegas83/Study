print('Задайте координату начала отрезка')
start = int(input())
print('Задайте координату конца отрезка')
end = int(input())
chet = 0
div3 = 0
div4 = 0
while start <= end:
    if start % 2 == 0:
        chet = chet+1
    if start % 3 == 0:
        div3 = div3+1
    if start % 4 == 0:
        div4 = div4+1
    start = start+1
print('Количество четных чисел:', chet)
print('Количество чисел, делящихся нацело на 3:', div3)
print('Количество чисел, делящихся нацело на 4:', div4)
