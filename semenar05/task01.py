"""
посчитать НОК наименьшее общее кратное и НОД наибольший общий делитель
"""
lst1 = []
lst2 = []


def ad(n, lst):
    numFactorial = 2
    while n > 1:
        if n % numFactorial == 0:
            lst.append(numFactorial)
            n = n // numFactorial
        else:
            numFactorial += 1


num1 = int(input('Введи число: '))
num2 = int(input('Введи число: '))
f(num1, lst1)
f(num2, lst2)
print(lst1, set(lst1))
print(lst2, set(lst2))
lstNod = (set(lst1).intersection(set(lst2)))

nod = 1
for i in lstNod:
    nod = nod * i

nok = (num1 * num2) / nod
print(ad'nod {nod} nok {nok}')
