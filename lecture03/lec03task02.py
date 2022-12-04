# def sum(x, y):
#     return x + y
# f = sum

sum = lambda x, y: x + y


def mylt(x, y):
    return x * y


def calc(op, a, b):
    print(op(a, b))
    # return op(a, b)


calc(mylt, 4, 5)
# calc(f, 4, 5)
calc(sum, 4, 4)
calc(lambda x, y: x + y, 4, 10)
