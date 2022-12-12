"""
посчитать НОК наименьшее общее кратное и НОД наибольший общий делитель
"""

# 1. разложить числа на простые множители

a, b = int(input('число А: ')), int(input('число B: '))
abMaxStr = []
abMinStr = []
cMin = 2
nok = 0

# посчитать НОК
numMin = abMin = min(a, b)
numMax = abMax = max(a, b)
if abMax % abMin == 0:
    print(f'НОК: {abMax}')
elif abs(a) < 10 and abs(b) < 10:
    print(f'НОК: {a * b}')
else:
    while abMax != 1:
        if abMax % cMin == 0:
            abMaxStr.append(cMin)
            abMax = abMax // cMin
            cMin = 2
        else:
            cMin += 1

    while abMin != 1:
        if abMin % cMin == 0:
            abMinStr.append(cMin)
            abMin = abMin // cMin
            cMin = 2
        else:
            cMin += 1
    print(abMaxStr)
    print(abMinStr)

for i in range(len(abMaxStr)):
    if abMaxStr[0] != abMinStr[0]:
        print(f'НОК: {numMax * abMinStr[i]}')
        break
    # print(abMaxStr[i], abMinStr[i])
    elif abMaxStr[i] != abMinStr[i]:
        print(f'НОК: {numMax * abMinStr[i]}')
        break

