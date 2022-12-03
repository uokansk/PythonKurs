"""
Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
между максимальным и минимальным значением дробной части элементов.
"""

lst = [1.1, 1.2, 3.1, 5.1, 10.01]
tenthLst = []
for i in lst:
    tenthLst.append(round(i % 1, 4))
print(tenthLst)
print(max(tenthLst) - min(tenthLst))
