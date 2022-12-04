# без файла
# def f(x):
#     return x ** 2
#
#
# lst = [1, 2, 3, 5, 8, 15, 23, 38]
# lst3 = [(i, f(i)) for i in lst if i % 2 == 0]
# print(lst3)

# с файлом
# f = open('file.txt', 'r')
# data = f.read() + ' '
# f.close()
# print(data)
# numbers = []
# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos + 1:]
# print(numbers)
# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e, e ** 2))
# print(out)


# сокращенное
# def select(f, col):
#     return [f(x) for x in col]  # формируем список
#
#
# def where(f, col):
#     return [x for x in col if f(x)]
#
#
# data = '1 2 3 5 8 15 23 38'.split()
# data = select(int, data)
# print(data)
# data = where(lambda e: not e % 2, data)
# print(data)
# data = list(select(lambda e: (e, e ** 2), data))
# print(data)

# с функцией map

# li = [x for x in range(1, 20)]
# print(li)
# li = list(map(lambda x: x + 10, li))
# print(li)
# data = '1 2 3 5 8 15 23 38'.split()
# data = list(map(int, data))
# data = list(filter(lambda e: not e % 2, data))
# data = list(map(lambda e: (e, e ** 2), data))
# print(data)

# data = list(map(int, input().split()))
# print(data)

# data = map(int, input().split())
# for i in data:
#     print(i)
# после этого возвращаемся на строку 29


# функция  select теперь не нужна

# def where(f, col):
#     return [x for x in col if f(x)]
#
# функцию where заменим функцией filter()
#
# data = '1 2 3 5 8 15 23 38'.split()
# data = list(map(int, data))
# print(data)
# data = where(lambda e: not e % 2, data)
# print(data)
# data = list(map(lambda e: (e, e ** 2), data))
# print(data)

# работа с функцией filter()

# data = [x for x in range(11)]
# print(data)
# # res = list(filter(lambda x: x % 2 == 0, data))
# # по питоновски будет так
# res = list(filter(lambda x: not x % 2, data))
# print(res)


# функцию where заменим функцией filter()
#
data = '1 2 3 5 8 15 23 38'.split()
data = list(map(int, data))
print(data)
data = list(filter(lambda e: not e % 2, data))
print(data)
data = list(map(lambda e: (e, e ** 2), data))
print(data)
