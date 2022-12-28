"""
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
"""

# number = -8
# lst = []
# for i in range(0, number, -1):
#     print(i)
#     lst.append((-1) ** (i + 1))
# print((-1)**(-0+1))
# print(lst)


# fib2 = 1
# fib1 = 1
# fib0 = 0
# fibM1 = 1
# fibM2 = -1
# n = 0
#
# lst = [fibM2, fibM1, fib0, fib1, fib2]
# for i in range(-2, -n, -1):
#     fibM1, fibM2 = fibM2, fibM1 - fibM2
#     lst.insert(0, fibM2)
# print(lst)
# for i in range(2, n, 1):
#     fib1, fib2 = fib2, fib1 + fib2
#     lst.append(fib2)
# print(lst)


fib0 = 0
fib1 = 1
lst = [fib0]
n = int(input('Введите число: '))

for i in range(1, n + 1):
    lst.append(fib1)
    fib0, fib1 = fib1, fib0 + fib1
fib0 = 0
fib1 = 1
for i in range(-1, -n - 1, -1):
    lst.insert(0, fib1)
    fib0, fib1 = fib1, fib0 - fib1
print(ad'Числа Фибоначчи для {n}, в том числе для отрицательных индексов {lst}')
