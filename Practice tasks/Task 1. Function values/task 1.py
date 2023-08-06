a, x, b, c = map(int, input().split(" "))


def func(a, x, b, c):
    y = a * x**2 + b * x + c
    return y


print(func(a, x, b, c))
