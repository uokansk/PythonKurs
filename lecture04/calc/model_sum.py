# метод отвечающий за  инициализацию x y

x = 0
y = 0


def ad(a, b):
    global x
    global y
    x = a
    y = b


def do_it():
    return x + y


# ad(11, 22)
# print(x, y)
