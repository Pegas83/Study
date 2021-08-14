print('Input a random number')
num = int(input())
x = ''
while num > 0:
    dig = num % 10
    x = x + str(dig)
    num = num // 10
print(x)