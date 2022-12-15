"""
на вход строка с арифметическим выражением, ответ - решение выражения
Напишите программу вычисления арифметического выражения заданного строкой.
Используйте операции +,-,/,*. приоритет операций стандартный.
Пример:
2 + 2 => 4;
1 + 2 * 3 => 7;
1 - 2 * 3 => -5;
"""

lst = '1 - 2 * 3 / 3'
lst = lst.split()


while len(lst) > 1:
    while '*' in lst or '/' in lst:
        if lst.count('*') > 0 and lst.count('/') > 0:
            if lst.index('/') > lst.index('*'):
                lst[lst.index('*') - 1] = int(lst[lst.index('*') - 1]) * int(lst[lst.index('*') + 1])
                lst.pop(lst.index('*') + 1)
                lst.pop(lst.index('*'))
            else:
                lst[lst.index('/') - 1] = int(lst[lst.index('/') - 1]) / int(lst[lst.index('/') + 1])
                lst.pop(lst.index('/') + 1)
                lst.pop(lst.index('/'))
        else:
            if '*' in lst:
                lst[lst.index('*') - 1] = int(lst[lst.index('*') - 1]) * int(lst[lst.index('*') + 1])
                lst.pop(lst.index('*') + 1)
                lst.pop(lst.index('*'))
            else:
                lst[lst.index('/') - 1] = int(lst[lst.index('/') - 1]) / int(lst[lst.index('/') + 1])
                lst.pop(lst.index('/') + 1)
                lst.pop(lst.index('/'))
    while '+' in lst or '-' in lst:
        if lst.count('+') > 0 and lst.count('-') > 0:
            if lst.index('-') > lst.index('+'):
                lst[lst.index('+') - 1] = int(lst[lst.index('+') - 1]) * int(lst[lst.index('+') + 1])
                lst.pop(lst.index('+') + 1)
                lst.pop(lst.index('+'))
            else:
                lst[lst.index('-') - 1] = int(lst[lst.index('-') - 1]) / int(lst[lst.index('-') + 1])
                lst.pop(lst.index('-') + 1)
                lst.pop(lst.index('-'))
        else:
            if '*' in lst:
                lst[lst.index('+') - 1] = int(lst[lst.index('+') - 1]) * int(lst[lst.index('+') + 1])
                lst.pop(lst.index('+') + 1)
                lst.pop(lst.index('+'))
            else:
                lst[lst.index('-') - 1] = int(lst[lst.index('-') - 1]) - int(lst[lst.index('-') + 1])
                lst.pop(lst.index('-') + 1)
                lst.pop(lst.index('-'))

print(lst)

