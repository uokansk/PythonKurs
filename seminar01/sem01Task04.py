"""
Напишите программу, которая по заданному номеру четверти,
показывает диапазон возможных координат точек в этой четверти (x и y).
"""

quarterNumber = int(input('Enter quarter: '))
if quarterNumber == 1:
    print('x > 0, y > 0')
elif quarterNumber == 2:
    print('x < 0, y > 0')
elif quarterNumber == 3:
    print('x < 0, y < 0')
elif quarterNumber == 4:
    print('x > 0, y < 0')
else:
    print('Проверте данные')
