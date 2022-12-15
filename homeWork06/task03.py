"""
Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях. Позиции хранятся
в файле file.txt в одной строке одно число.
"""

import math

# n = int(input('Введите число: '))
f = open('file.txt')
data = f.read()
f.close()

# lst = [n for n in range(-n, n+1)]


lst2 = [line for line in data]
print(lst2)
exit()
for line in data:
    sumNumber *= lst[int(line)]
    print('данные из файла ', line, end='')
    # for i in lst:
    #     if int(line) == lst.index(i):
    #         sumNumber *= i
print('\n', 'список из', n, 'элементов', lst)
print('произведение элементов ', sumNumber)


data = [x for x in range(10)]
print(data)