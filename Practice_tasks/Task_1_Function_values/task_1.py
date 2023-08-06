a, x, b, c = map(
    int, input().split(" ")
)  # writing as variables entered by user numbers


def func(a, x, b, c):  # func to calculate result according to assignment
    y = a * x**2 + b * x + c
    return y


print(func(a, x, b, c))  # output result of func
