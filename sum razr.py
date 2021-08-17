print('Введите 3-х значное число')
num = int(input())
a = num//100
b = (num-a*100)//10
c = num % 10
if num % (a+b+c) == 0:
    print('Делится')
    print('Делится')
else:
    print('Не делится')
print(a+b+c)