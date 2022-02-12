def add_x(f):
    f[0][0] = 'x'
    return f


field_1 = [['_'] * 4 for i in range(4)]   # 1 способ
print(add_x(field_1))

field_2 = [['_'] * 4] * 4   # 2 способ
print(add_x(field_2))
