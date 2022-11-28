"""
Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях. Позиции хранятся
в файле file.txt в одной строке одно число.
"""


n = int(input('Введите число: '))
lst = []
data = open('file.txt')
sumNumber = 1
for i in range(-n, n + 1):
    lst.append(i)

for line in data:
    print('данные из файла ', line, end='')
    for i in lst:
        if int(line) == lst.index(i):
            sumNumber *= i
print('\n', 'список из', n, 'элементов', lst)
print('произведение элементов ', sumNumber)
data.close()
