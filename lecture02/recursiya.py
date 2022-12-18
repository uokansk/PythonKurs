# в рекурсии главное указать в какой момент остановиться

def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)  # здесь идет рекурсия


list = []
for e in range(1, 8):
    list.append(fib(e))
print(list)  # 1 1 2 3 5 8 13 21 34
