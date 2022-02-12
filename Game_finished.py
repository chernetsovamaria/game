import random


def welcome_speech(c, s):
    print(f'''Добро пожаловать в игру!
Вы можете перемещаться по полю с помощью команд:
{c}
Если вы хотите выйти из игры, напишите {s}''')


def size_input():
    s = int(input('Введите размер поля: '))
    return s


def make_field(s):
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


def add_x(f):
    ver = 0
    hor = 0
    f[ver][hor] = 'x'
    return f, ver, hor


def field_output(f):
    print('Ваше текущее местоположение: ')
    for i in f:
        print(' '.join(i))


def command_input():
    c = input('Введите команду: ').lower()
    return c


def move_x(cs, c, f, v, h, s):
    limit = 'Вы достигли края поля, выберите другую команду.'
    barrier = 'Впереди препятствие, выберите другую команду.'
    if c == cs[0]:   # вверх
        if v - 1 < 0:
            print(limit)
        elif f[v - 1][h] == 'o':
            print(barrier)
        else:
            f[v - 1][h] = 'x'
            f[v][h] = '_'
            v -= 1
    elif c == cs[1]:   # вниз
        if v + 1 > s - 1:
            print(limit)
        elif f[v + 1][h] == 'o':
            print(barrier)
        else:
            f[v + 1][h] = 'x'
            f[v][h] = '_'
            v += 1
    elif c == cs[2]:   # направо
        if h + 1 > s - 1:
            print(limit)
        elif f[v][h + 1] == 'o':
            print(barrier)
        else:
            f[v][h + 1] = 'x'
            f[v][h] = '_'
            h += 1
    elif c == cs[3]:   # налево
        if h - 1 < 0:
            print(limit)
        elif f[v][h - 1] == 'o':
            print(barrier)
        else:
            f[v][h - 1] = 'x'
            f[v][h] = '_'
            h -= 1

    return f, v, h


def last_speech():
    print('Вы завершили иргу!')


def game():
    commands = ('up', 'down', 'right', 'left')
    stop_word = 'stop'
    welcome_speech(commands, stop_word)
    process = True
    size = size_input()   # размер игр. поля
    field, ver_x, hor_x = add_x(make_field(size))   # игр. поле, коор. 'x' по верт. и гор.
    while process:
        field_output(field)   # вывод текущего положения 'x'
        command = command_input()   # ввод команды
        if command == stop_word:
            last_speech()
            break
        field, ver_x, hor_x = move_x(commands, command, field, ver_x, hor_x, size)   # перемещение 'x'


game()
