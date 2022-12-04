def f(x):
    return x ** 2


g = f


# print(f(2))
# print(g(6))
# print(type(f))

def calc1(x):
    return x + 10


def calc2(x):
    return x * 10


def math(op, x):
    print(op(x))


math(calc2, 5)
math(calc1, 5)

print(calc1(10))
print(calc2(10))
