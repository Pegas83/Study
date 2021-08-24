list = [1, 2, 3, 8, 2, 2, 8, -1, 7, -1, 110]
list_of_reps = []
for i in range(0, len(list), 1):
    repeat = 0
    for j in range(0, len(list), 1):
        if list[j] == list[i]:
            repeat = repeat + 1
    list_of_reps.append(repeat)
print(list_of_reps)







