"""
Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
В качестве символа-разделителя используйте пробел.
"""

lst = '2 3 4 5 6 7'
lst2 = []
for i in lst.split():
    lst2.append(int(i))
print(lst2)
print(min(lst2), max(lst2))

# второй способ
lst2 = [float(i) for i in lst.split()]
print(min(lst2), max(lst2))
