# import hello # обращаемся к файлу hello.py
# или

# print(hello.f(2.3))


# import hello as h
#
# print(h.f(2.3))

# def new_string(symbol, count):
#     return symbol * count
#
#
# print(new_string('!', 5))  # !!!!!
# print(new_string('!'))  # TypeError missing 1 required ... #  если знаение не задать, выйдет ошибка

# но можно задать значение  по умолчанию

# def new_string(symbol, count=3):
#     return symbol * count
#
#
# print(new_string('!', 5))  # !!!!!
# print(new_string('!'))  # !!!
# print(new_string(4))  # 12


# неограниченное количество аргументов
# для этого ставим (*params)

def conn(*params):
    res: str = ""
    for i in params:
        res += i
    return res


print(conn('a', 'b', 'c', 'd'))
