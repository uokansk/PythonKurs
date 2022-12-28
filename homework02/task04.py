"""
Задайте список из x_or_o элементов, заполненных числами из промежутка [-x_or_o, x_or_o].
Найдите произведение элементов на указанных позициях. Позиции хранятся
в файле file.txt в одной строке одно число.
"""

n = int(input('Введите число: '))
# lst = []
data = open('file.txt')
sumNumber = 1
# for i in range(-n, n + 1):
#     lst.append(i)
f = open('f.txt', 'r')
data = f.read() + ' '
f.close()


lst = [n for n in range(-n, n+1)]
print(lst)
exit()

lst2 = [line for line in data]
for line in data:
    sumNumber *= lst[int(line)]
    print('данные из файла ', line, end='')
    # for i in lst:
    #     if int(line) == lst.index(i):
    #         sumNumber *= i
print('\n', 'список из', n, 'элементов', lst)
print('произведение элементов ', sumNumber)
data.close()
