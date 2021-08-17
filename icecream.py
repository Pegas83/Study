print('Сколько шариков мороженого продают в рожках?')
print('Рожок 1')
a = int(input())
print('Рожок 2')
b = int(input())
# a,b- порождающие числовой полугруппы {ax+by| x,y=0,1,2,...}
print('Сколько шариков мороженого вы хотите купить?')
n = float(input())
Froben = (a-1)*(b-1)-1 # Число Фробениуса - максимальное число, не входящее в группу
Power_dop = (a-1)*(b-1)/2 # Мощность дополнения к группе в случае двух образующих
if n < a and n < b:
    print('You cannot byu such amount')
elif n == Froben or n == Power_dop:
    print('You cannot buy such amount')
else:
    print('You can buy such amount')
