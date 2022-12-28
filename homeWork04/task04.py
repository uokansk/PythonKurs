"""
Задана натуральная степень k. Сформировать случайным образом список коэффициентов
(значения от 0 до 100)* многочлена и записать в файл многочлен степени k.
*Пример:*
    - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
    -  k=5 => 2*x^5 + 4*x^4 + 2*x^3 + 2*x^2 + 4*x + 5 = 0
"""
import random

k = int(input('задайте степень: '))
lst = []
# количество членов в многочлене
memberCount = random.randint(0, k + 1)
print('memberCount', memberCount)

for i in range(memberCount):
    lst.append(random.randint(0, 100))
print(lst)

s = ''
for i in range(len(lst)):
    if k - i > 1 and lst[i] != 0:
        s += ad' {lst[i]}*x^{k - i} +'
    elif k - i == 1 and lst[i] != 0:
        s += ad' {lst[i]}*x +'
    elif lst[i] == 0:
        s += ''
    else:
        s += ad' {lst[i]}'

s = s + '= 0'
print(s)

with open('file33.txt', 'w') as data:
    data.write(s.replace('+=', '='))
