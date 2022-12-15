"""
Напишите программу, которая принимает на вход вещественное число и
показывает сумму его цифр.(Сделать для строки)
"""
import math
n = str(input('Введите число: ')).replace('.', '')
# n = n.replace('.', '')
# print(n)
number = 0
# for c in n:
#     number += int(c)
# print(number)
def f(x):
    return x+=x

lst = [f(i) i for i in n]
print(lst)