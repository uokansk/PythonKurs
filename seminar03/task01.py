"""
реализуйте алгоритм перемешивания списка без рандом
"""
import time


def randNum(minN=0, maxN=10):
    number = int((time.time() % 1) * (maxN - minN) + minN)
    return number


lst = [2, 10, -5, 8, 46]
# print(random.shuffle(lst))
print(lst)
for i in range(len(lst)):
    j = randNum(0, len(lst) - 1)
    lst[i], lst[j] = lst[j], lst[i]
print(lst)
