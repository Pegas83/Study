place_x = 0
place_y = 0
while place_x != 30 and place_y != 20:
    print('Enter the direction: N,W,E,S')
    way = str(input())
    print('Enter the amount of steps')
    steps = int(input())
    if way == 'N':
        place_y = place_y + steps
        if place_y > 50:
            print('You are leaving the search area. Try another direction or amount of steps')
            place_y = place_y - steps
        print(place_x, '  ', place_y)
    if way == 'S':
        place_y = place_y - steps
        if place_y < 0:
            print('You are leaving the search area. Try another direction or amount of steps')
            place_y = place_y + steps
        print(place_x, '  ', place_y)
    if way == 'W':
        place_x = place_x - steps
        if place_x < 0:
            print('You are leaving the search area. Try another direction or amount of steps')
            place_x = place_x + steps
        print(place_x, '  ', place_y)
    if way == 'E':
        place_x = place_x + steps
        if place_x > 50:
            print('You are leaving the search area. Try another direction or amount of steps')
            place_x = place_x - steps
        print(place_x, '  ', place_y)
print('Congratulations! You found treasure')