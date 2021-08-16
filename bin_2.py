print('Enter a random number')
num = float(input())
num_binary = []
true = []
while num != 0:
    dig = num - (num // 2) * 2
    num_binary.append(dig)
    num = num // 2
for i in range(len(num_binary) - 1, -1, -1):
    true.append(num_binary[i])
print(true)
print(type(true))



