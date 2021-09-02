dictionary = {
              'Ivanov Ivan Ivanovich': '01.05.1965',
              'Petrov Petr Petrovich': '02.06.1970',
              'Sidorov Ivan Petrovich': '03.07.1980',
              'Ivanova Olga Dmitrievna': '06.10.1991',
              'Nikolaeva Svetlana Vladimirovna': '10.08.1989'
             }
years = []  # list with a years of birth(int)
for value in dictionary.values():
    razr = 1000
    sum = 0
    year = 0
    for i in range(len(value)-4, len(value), 1):
        year = year + int(value[i])*razr
        razr /= 10
    years.append(year)
'''Counting the oldest and the youngest'''
the_youngest = years[0]
the_oldest = years[0]
for year in years:
    if year > the_youngest:
        the_youngest = year
    if year < the_oldest:
        the_oldest = year
'''Counting the middle-aged'''
middle = (the_youngest + the_oldest) / 2
diff_mid = [] #list contains differences between years and middle year
for k in range(len(years)):
    diff_mid.append(abs(years[k] - middle))
min_diff = diff_mid[0]
index = 0
for k in range(len(diff_mid)):
    if diff_mid[k] < min_diff:
        min_diff = diff_mid[k]
        index = k
the_middle_aged = years[index]
'''Output'''
for key in dictionary.keys():
    if dictionary[key][6:10] == str(int(the_middle_aged)):
        print(key, '- middle age')
    if dictionary[key][6:10] == str(int(the_youngest)):
        print(key, '- the youngest')
    if dictionary[key][6:10] == str(int(the_oldest)):
        print(key, '- the oldest')