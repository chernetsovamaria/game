import random
from random import randint


def directions():
    d = ('вверх', 'вниз', 'направо', 'налево')
    return d


def welcome_speech(v, stop):
    s = str(v).replace("(", "").replace(")", "").replace("'", "")
    print(f'''Приветствуем вас в игре!
вы можете перемещаться по полю в следующих направлениях: {s}
Для выхода из игры напишите {stop}''')


def create_playing_field(s):
    template = []
    list_of_temp = []
    for i in range(s):
        for e in range(s):
            num = random.randint(0, 1)
            if num:
                template.append('o')
            else:
                template.append('_')
        list_of_temp.append(template)
        template = []
    return list_of_temp


def starting_position(s):
    s[0][0] = 'x'
    v = 0
    h = 0
    return s, v, h


def user_input():
    s = int(input('Введите размер поля: '))
    return s


def current_position(s, f):
    print('Ваше текущее положение: ')
    for i in range(s):
        position = str(f[i]).replace(" ", "").replace(",", "").replace("[", "").replace("]", "").replace("'", "")
        print(position)


def second_speech():
    d = input('Выберите направление:').lower()
    return d


def moving(d, f, v, vert, hor, s, p):
    barrier = 'О нет, впереди препятствие!'
    limit_reached = 'Вы вышли за пределы поля.'
    if d == v[0]:
        vert -= 1
        if vert < 0:
            print(limit_reached)
            vert += 1
        elif f[vert][hor] == 'o':
            print(barrier)
            vert += 1
        f[vert][hor] = 'x'
        f[vert + 1][hor] = '_'
    elif d == v[1]:
        vert += 1
        if vert > s - 1:
            print(limit_reached)
            vert -= 1
        elif f[vert][hor] == 'o':
            print(barrier)
            vert -= 1
        f[vert][hor] = 'x'
        f[vert - 1][hor] = '_'
    elif d == v[2]:
        hor += 1
        if hor > s - 1:
            print(limit_reached)
            vert -= 1
        elif f[vert][hor] == 'o':
            print(barrier)
            vert -= 1
        f[vert][hor] = 'x'
        f[vert - 1][hor] = '_'
    elif d == v[3]:
        hor -= 1
        if hor < 0:
            print(limit_reached)
            vert += 1
        elif f[vert][hor] == 'o':
            print(barrier)
            vert += 1
        f[vert][hor] = 'x'
        f[vert + 1][hor] = '_'
    elif d == stop_word:
        print('Вы завершили игру!')
        p = False
    return f, p


def game():
    variants = directions()  # варианты направления
    process = True
    stop_word = 'выход'
    welcome_speech(variants, stop_word)  # приветствие
    size = user_input()  # размер поля
    field = create_playing_field(size)  # создание поля с препятсвиями (вложенный список)
    field, vertical_position, horizontal_position = starting_position(
        field)  # начальная позиция 'x', номер списка с 'x'
    while process:
        current_position(size, field)  # вывод текущего положения
        direction = second_speech()  # выбор направления
        field = moving(direction, field, variants, vertical_position, horizontal_position, size, process)


game()