"""
Реализуйте алгоритм нахождения(генерации) рандомного(случайного) числа.
(Не используя библиотеки связанные с рандомом)
"""
# import time


"""
first variant
"""
import time

first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
randomNum = int(round((time.time() % 1) * (second - first) + first, 0))
print(ad'случайное число {first} до {second} это {randomNum}')
# print(time.time() % 1)
# print(time.time())

# import datetime

# print(datetime.datetime.now())
# print(datetime.datetime.now().microsecond)
