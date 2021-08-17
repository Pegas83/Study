print('Введите трехзначное число')
y = int(input())
x=y
a = x%10
x = x//10
b = x%10
c = x//10
sum = a+b+c
ost = y%sum
print(ost)

