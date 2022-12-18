value = None
# print(type(value))
a = 123
b = 1.23
# print(a)
# print(b)
value = 12456
print(value)

# узнать тип данных type()

# print(type(a))
# print(type(b))
value = 12456
# print(type(value))

s = 'hello world'
print(s)

# в строку можно ввести апостраф
s = 'hello \"world\"'
print(s)

# интерполяция
print(a, b, s)
print(a, '-', b, '-', s)
print('{} - {} - {}'.format(a, b, s))
print(f'{a} - {b} - {s}')
print('{1} - {2} - {0}'.format(a, b, s))

f = True
print(f)

# списки
lst = [1, 2, 3, 4]
lst2 = ['1', '2', '3', '4']
print(lst)
print(lst2)

# ввод данных

# a = input('ввод a :')
# b = input('ввод b :')
# print(a + b)

# a = int(input('ввод a :'))
# b = int(input('ввод b :'))
# print(a + b)

# Арифметические операции
# +, -, *, /, %, //, **

a = 1.31256255687
b = 3
c = round(a * b, 7)  # округление
print(c)

# операции присваивания
a = 5
a += 10
print(a)
