"""
Задайте список из нескольких чисел. Напишите программу,
которая найдёт сумму элементов списка, стоящих на нечётной позиции.
"""

lst = [2, 3, 5, 9, 3]
sumNum = 0
for i in range(1, len(lst), 2):
    sumNum += lst[i]
print(ad'сумма чисел стоящих на нечётной позиции {sumNum}')
