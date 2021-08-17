print('Enter a random number')
num = int(input())
num_binary = []
result = ''
while num != 0:
    dig = num % 2
    num_binary.append(dig)
    num = num // 2
for i in range(len(num_binary) - 1, -1, -1):
    result = result + str((num_binary[i]))
print(result)




