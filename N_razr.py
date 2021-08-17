print('Задайте случайное число')
var = int(input())
"""k = 10
i = 1
x = 0
test = 0
while test < var:
    x = (var % k) // i
    print(x)
    k = k*10
    test = test + i * x
    i = i*10"""

while var > 0:
    print(var % 10)
    var = var // 10
