"""
Задача №41: Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах. Пример:
На сжатие входные данные: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
Выходные данные:          12W1B12W3B24W1B14W
"""

import itertools
print("".join([k+str(len(list(g))) for k, g in itertools.groupby(input())]))
