"""
Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
"""
n = int(input('Введите число: '))
factorial = 1
list_fact = []
for i in range(1, n+1):
    factorial *= i
    list_fact.append(factorial)
print('набор произведений чисел от 1 до', n, list_fact)
