dictionary = {1: [11, 2, 3],
              2: [36, -110],
              3: [245],
              4: [-23, 34, 60],
              5: [-120, 1, 2]
              }
print(dictionary)
for i in range(1, 5, 1):
    index = i
    num_list = []
    for k in range(len(dictionary[i])):
        num_list.append(int(dictionary[i][k]))
    min = 0
    for l in range(len(num_list)):
        min += num_list[l]
    for m in range(i, 6, 1):
        num_list = []
        for k in range(0, len(dictionary[m]), 1):
            num_list.append(int(dictionary[m][k]))
        sum = 0
        for l in range(len(num_list)):
            sum += num_list[l]
        if sum <= min:
            index = m
            min = sum
    temp = dictionary[i]
    dictionary[i] = dictionary[index]
    dictionary[index] = temp
print('Sorted dictionary:', dictionary)


