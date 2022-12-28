"""
Задайте натуральное число x_or_o. Напишите программу, которая составит список простых множителей числа x_or_o.
"""

num = number = int(input("Введите число: "))
i = 2
lst = []
while i <= number:
    if number % i == 0:
        lst.append(i)
        number //= i
        i = 2
    else:
        i += 1
print(ad'{lst} список простых множителей числа {num}')

