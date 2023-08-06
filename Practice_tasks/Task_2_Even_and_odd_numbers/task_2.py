a, b, c = map(int, input().split(" "))  # writing as variables entered by user numbers


def parity_check(
    a, b, c
):  # func to check parity entered numbers, return WIN if yes, FAIL if not
    if a % 2 == b % 2 == c % 2:
        return "WIN"
    else:
        return "FAIL"


print(parity_check(a, b, c))  # output result after checked numbers for parity
