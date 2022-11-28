# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors)  # разделителей не будет
# data.write('\nLine 2\n')
# data.write('\nLine 3\n')
# data.close()


# with open('file.txt', 'a') as data:
#     data.write('line 11111\n')
#     data.write('line 22222\n')


# path = 'text.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# import hello as h
# print(h.f(2.3))


# def new_string(symbol, count=3):
#     return symbol * count
#
#
# print(new_string('!', 5))  # !!!!!
# print(new_string('!'))  # !!!
# print(new_string(4))  # 12

# def concatenation(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res
#
#
# print(concatenation('a', 's', 'd', 'w'))  # asdw
# print(concatenation('a', '1', 'd', '2'))  # a1d2

# Рекурсия

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
#
#
# list = []
# for e in range(1, 5):
#     list.append(fib(e))
# print(list)  # 1 1 2 3 5 8 13 21 34

# Кортежи
# a, b = 3, 4
# print(a, b)

a = (3, 4)
print(a)
print(a[0])
