# введение данных строкой через пробел
a, b = input('введите числа через пробел: ').split(' ')
print(a, b)
print(int(a) + int(b))
