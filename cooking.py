print('Введите количество купленных котлет')
m = float(input())
print('Введите количество  котлет, помещающихся на сковороду')
n = float(input())
print('Введите время, за которое прожаривается одна сторона котлеты')
t = int(input())
#part = m/n
#time = part
if m % n == 0:
    part = m//n
else:
    part = (m//n)+1
time1 = t*2
time = part*time1
print('Минимальное ремя, за которое можно пожарить все котлеты:', time)
