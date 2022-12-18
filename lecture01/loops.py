# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)
#
# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
#     print(inverted, original)
# else:
#     print('Пожалуй хватит')
# print(inverted)

# for i in 1, 2, 3, 4, 5:
#     print(i ** 2)
#
# # or
#
# lst = [1, 2, 3, 4, 5]
# for i in lst:
#     print(i)

# range

r = range(5)
for i in r:
    print(i)
# or
print()
for i in range(5):
    print(i)

print()
for i in range(1, 10, 2):  # начало конец и шаг итераций
    print(i)

# можно со строками
print(' можно и со строками ')
for i in 'qwerty':
    print(i)

# длина строки

text = 'можно и со строками'
print(len(text))
print('и ' in text)
print(text.isdigit())
print(text.islower())
print(text.replace('о', 'ОО'))
