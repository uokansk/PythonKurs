lst = []
for i in range(1, 25):
    if i % 2 == 0:
        lst.append(i)

print(lst)

# то же самое, что и в верху
lst2 = [i for i in range(1, 25) if i % 2 == 0]
print(lst2)

# для получения кортежей
lst2 = [(i, i) for i in range(1, 21) if i % 2 == 0]
print(lst2)


# используем функцию
def f(x):
    return x ** 3


lst2 = [f(i) for i in range(1, 13) if i % 2 == 0]
print(lst2)
# с кортежами
lst3 = [(i, f(i)) for i in range(1, 13) if i % 2 == 0]
print(lst3)
#####################
