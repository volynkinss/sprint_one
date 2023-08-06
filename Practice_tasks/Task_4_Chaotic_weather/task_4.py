n = int(input())
temperature_values = list(map(int, input().split(" ")))


def chaotic_days(n, temperature_values):
    chaotic_days = 0
    if n == 1:
        chaotic_days += 1
        return chaotic_days
    for i in range(n):
        if i == 0:
            if temperature_values[i] > temperature_values[i + 1]:
                chaotic_days += 1
        elif i == n - 1:
            if temperature_values[i] > temperature_values[i - 1]:
                chaotic_days += 1
        else:
            if (
                temperature_values[i] > temperature_values[i - 1]
                and temperature_values[i] > temperature_values[i + 1]
            ):
                chaotic_days += 1
    return chaotic_days


print(chaotic_days(n, temperature_values))
