print('Введите координату точки A')
a = int(input())
print('Введите координату точки B')
b = int(input())
print('Введите координату точки C')
c = int(input())
if (b-a) < (c-a):
    print('Точка В с координатой', b, 'находится ближе к точке А')
else:
    print('Точка C с координатой', c, 'находится ближе к точке А')