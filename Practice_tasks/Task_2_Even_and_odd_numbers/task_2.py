a, b, c = map(int, input().split(" "))


def parity_check(a, b, c):
    if a % 2 == b % 2 == c % 2:
        return "WIN"
    else:
        return "FAIL"


print(parity_check(a, b, c))
