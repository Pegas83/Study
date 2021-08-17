print('Введите коэффициенты a, b, c квадратного уравнения вида ax^2+bx+c=0, где а отлично от нуля')
print('a=')
a = float(input())
print('b=')
b = float(input())
print('c=')
c = float(input())
if a == 0:
    print('Данное уравнение не относится к квадратным. Повторно задайте коэффициенты уравнения')
else:
    if b != 0 and c == 0:
        x1 = 0
        x2 = -b/a
        print('Уравнение имеет два корня: х1=', x1, '; x2=', x2)
    elif b == 0 and c != 0:
        if c/a > 0:
            print('Уравнение решения не имеет')
        else:
            x1 = (-c/a)**(1/2)
            x2 = -(-c/a)**(1/2)
            print('Уравнение имеет два корня: х1=', x1, '; x2=', x2)
    else:
        D = b**2-4*a*c
        if D > 0:
            x1 = (-b-D**(1/2))/(2*a)
            x2 = (-b+D**(1/2))/(2*a)
            print('Уравнение имеет два корня: х1=', x1, '; x2=', x2)
        elif D == 0:
            x1 = -b/(2*a)
            print('Уравнение имеет единственный корень x', x1)
        else:
            print('Уравнение не имеет вещественных корней')
