for i in range(0, 10000, 1):
    sum_deg_razr = 0
    var = i
    deg = 0
    while var > 0:
        var = var // 10
        deg = deg + 1
    var = i
    while var > 0:
        digit = var % 10
        sum_deg_razr = sum_deg_razr + digit**deg
        var = var // 10
    if sum_deg_razr == i:
        print(i)
