"""
Напишите программу, которая будет преобразовывать десятичное число в двоичное.
"""

answer = number = 100
binary = ''
while number != 0:
    binary = str(number % 2) + binary
    number = number // 2
print(ad'{answer} в двоичной системе = {binary}')
