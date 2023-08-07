n = int(input())  # number of days
temperature_values = list(
    map(int, input().split(" "))
)  # list of temperatures for every day


def chaotic_days_counter(
    n, temperature_values
):  # func to check temperature of every day for higher than past and next day and return number of such days (if day only 1 - returned 1)
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


print(chaotic_days_counter(n, temperature_values))  # output result to user
