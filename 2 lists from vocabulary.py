dictionary = {
              'Ivanov Ivan Ivanovich': '01.05.1965',
              'Petrov Petr Petrovich': '02.06.1970',
              'Sidorov Ivan Petrovich': '03.07.1980',
              'Ivanova Olga Dmitrievna': '06.10.1991',
              'Nikolaeva Svetlana Vladimirovna': '10.08.1989',
              'Sergeev Nikolai Pavlovich': '23.08.2001'
             }
first_half_list = []
second_half_list = []
dict_to_list = list(dictionary.items())
for i in range(0, int(len(dictionary) / 2), 1):
    first_half_list.append(dict_to_list[i])
for i in range(int(len(dictionary) / 2), len(dictionary), 1):
    second_half_list.append(dict_to_list[i])
print('The first half list:')
for elem in first_half_list:
    print(elem)
print()
print('The second half list:')
for elem in second_half_list:
    print(elem)