"""
Задайте словарь из n чисел последовательности (1 + (1/n))^n и выведите на  экран их сумму.
"""

n = int(input('Введите индекс: '))
dictionary = {}
sumNumber = 0
for i in range(1, n + 1):
    dictionary[i] = round(float((1 + (1 / i)) ** i), 2)
    sumNumber += dictionary[i]
print('Значения словаря', dictionary)
print('Сумма значений словаря = ', round(sumNumber, 2))
