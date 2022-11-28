"""
Напишите программу, которая принимает на вход вещественное число и
показывает сумму его цифр.(Сделать для строки)
"""
# n = float(input('Введите число: '))
# count = 0
# while n % 1 != 0:
#     n *= 10
#     print(n)
# while n > 0:
#     a = n % 10
#     n = n // 10
#     count += a
#     print(a)
# print(count)

n = str(input('Введите число: '))
n = n.replace('.', '')
number = 0
for c in n:
    number += int(c)
print(number)
