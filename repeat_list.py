changing_list = [1, 1, 2, 8, 2, 2, 8, 6, 7, -1, 8]
const_list = changing_list
for i in range(0, len(changing_list), 1):
    compare = changing_list[i]
    repeat = 0
    for j in range(i, len(const_list), 1):
        if const_list[j] == compare:
            repeat = repeat + 1
    for j in range(i, len(const_list), 1):
        if const_list[j] == compare:
            changing_list[j] = str(repeat)
    print(changing_list)







