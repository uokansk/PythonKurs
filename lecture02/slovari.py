# Словари - Неупорядоченные коллекции произвольных объектов с доступом по ключу

# dictionary = {}
dictionary = \
    {
        'up': '↑',
        'left': '←',
        'down': '↓',
        'right': '→'
    }
# print(dictionary)  # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left'])  # ←
# print(dictionary['↑'])

for i in dictionary.keys():
    print(i)

for i in dictionary.values():
    print(i)

for i in dictionary:
    print(i)

for i in dictionary:
    print(dictionary[i])

#  замена элементов в словаре
dictionary['up'] = '+'
print(dictionary)