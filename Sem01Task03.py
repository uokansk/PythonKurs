"""
Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
"""

x = float(input('Enter X: '))
y = float(input('Enter y: '))
if x > 0 and y > 0:
    print('1')
elif x > 0 and y < 0:
    print('4')
elif x < 0 and y < 0:
    print('3')
elif x < 0 and y > 0:
    print('2')
else:
    print('Проверте данные')
