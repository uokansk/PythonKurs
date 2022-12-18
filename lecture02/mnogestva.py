# Множества - Неупорядоченная совокупность элементов

a = {1, 2, 3, 5, 8}
b = {'2', '5', 8, 13, 21}
print(type(a))  # set
print(type(b))  # set

a.add('88')  # добавляем элементы в конец множества
print(a)
a.add(88)
print(a)

a.remove(2)  # удаляем элементы в конец множества
print(a)

a.discard(2)  # удаляем элементы которых не существует не вызывая ошибки
print(a)

# a.clear()  # очищает множество

c = a.copy()  # копировать множество
u = a.union(b)  # объеденять множество
print(c, u)

i = a.intersection(b)  # i = {8, 2, 5}
dl = a.difference(b)  # dl = {1, 3}
dr = b.difference(a)  # dr = {13, 21}
