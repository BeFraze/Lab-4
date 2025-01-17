items = [['r', 3, 25],
        ['p', 2, 15],
        ['a', 2, 15],
        ['m', 2, 20],
        ['i', 1, 5],
        ['k', 1, 15],
        ['x', 3, 20],
        ['t', 1, 25],
        ['f', 1, 15],
        ['d', 1, 10],
        ['s', 2, 20],
        ['c', 2, 20]
]

items = sorted(items, key=lambda x: (x[2] / x[1], x[1]), reverse=True)
capacity = 9
place = 0
cost = 10
problem = [''' 'i', 'd' ''']
bag = ''

if problem:
    filtered_items = []
    for item in items:
        if item[0] in problem:
            place += item[1]
            cost += item[2]
            bag = bag + item[0] * int(item[1])
        else:
            filtered_items.append(item)
    items = filtered_items

for item in items:
    if place + item[1] <= capacity:
        place += item[1]
        cost += item[2]
        bag = bag + item[0] * int(item[1])
    else:
        cost -= item[2]

print('Итоговые очки выживания:',cost)
print('Том возьмет с собой:')
for i in range(0, capacity, 3):
    print(bag[i], bag[i+1], bag[i+2])

print('\nДоп задание:')

capacity = 7
place = 0
cost = 10
problem = [''' 'i', 'd' ''']
bag = ''

if problem:
    filtered_items = []
    for item in items:
        if item[0] in problem:
            place += item[1]
            cost += item[2]
            bag = bag + item[0] * int(item[1])
        else:
            filtered_items.append(item)
    items = filtered_items

for item in items:
    if place + item[1] <= capacity:
        place += item[1]
        cost += item[2]
        bag = bag + item[0] * int(item[1])
    else:
        cost -= item[2]

print('Итоговые очки выживания для 7 ячеек:',cost)
print('Том возьмет с собой:')
for i in range(0, capacity):
    print(bag[i], end = ' ')

if cost<=0:
    print('\nРешение для 7 ячеек отсутствует')
