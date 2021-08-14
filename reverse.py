print('Input a random number')
num = int(input())
dig_list = []
order = 1
reverse_num = 0
while num > 0:
    dig = num % 10
    dig_list.append(dig)
    num = num // 10
for i in range(len(dig_list)-1, -1, -1):
    reverse_num = reverse_num + dig_list[i]*order
    order = order * 10
print(reverse_num)
