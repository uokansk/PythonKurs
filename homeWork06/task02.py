"""
Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
"""
import math

# n = int(input('Введите число: '))
# factorial = 1

# list_fact = []

# for i in range(1, n + 1):
#     factorial *= i
#     list_fact.append(factorial)
# print('набор произведений чисел от 1 до', n, list_fact)


list_fact = math.prod(i for i in range(1, int(input('Введите число: ')) + 1))
print(list_fact)
