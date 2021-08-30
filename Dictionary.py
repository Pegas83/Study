dictionary = {'Ivanov Ivan Ivanovich': '01.05.1965', 'Petrov Petr Petrovich': '02.06.1970',
              'Sidorov Ivan Petrovich': '03.07.1980', 'Ivanova Olga Dmitrievna': '06.10.1991',
              'Nikolaeva Svetlana Vladimirovna': '10.08.1989'}
years_float = []  # list with a years of birth(int)
for value in dictionary.values():
    years = [] #list with a year of birth(string)
    razr = 1000
    sum = 0
    year = 0
    #    print(value)
    for i in range(len(value)-4, len(value), 1):
        years.append(value[i])
    for number in years:
        year = year + float(number)*razr
        razr /= 10
#        print(type(value[i]))
    years_float.append(year)
print(years_float)
'''                         Counting the oldest and the youngest'''
the_youngest = years_float[0]
the_oldest = years_float[0]
for year in years_float:
    if year > the_youngest:
        the_youngest = year
    if year < the_oldest:
        the_oldest = year
#print(the_youngest)
#print(the_oldest)
'''                         Counting the middle-aged'''
middle = (the_youngest + the_oldest) / 2
#print(middle)
dif_mid = [] #list contains differences between years and middle year
for k in range(len(years_float)):
    dif_mid.append(abs(years_float[k] - middle))
#print(dif_mid)
min_dif = dif_mid[0]
index = 0
for k in range(len(dif_mid)):
    if dif_mid[k] < min_dif:
        min_dif = dif_mid[k]
        index = k
#print(years_float[index])
the_middle_aged = years_float[index]
'''                         Output'''
