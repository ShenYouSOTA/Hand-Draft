basic_info = input("").split()
raw_series = input("").split()
"""
n: The length of the sequence.
m: The number of operations. 
P: The divisor in modulo operation.
"""

n, m, P = int(basic_info[0]), int(basic_info[1]), int(basic_info[2])

series: list = [int(num) for num in raw_series]


def update(factor: str) -> None:
    factor: list = factor.split()
    print(factor)
    k = int(factor[1])
    x = int(factor[2])
    y = int(factor[3])
    c = int(factor[4])
    temp = x ** 2 + k * y + 5 * x
    series[k - 1] = (temp % P) * c


def sum_sequence() -> None:
    summation = sum(series)
    print(summation)


def distinct_value() -> None:
    value = 0
    distinct_set = []
    for i in range(n):
        tempo = series[i]
        if tempo in distinct_set:
            tempo = tempo * (-1)
            if tempo in distinct_set:
                continue
            else:
                distinct_set.append(tempo)
                value += 1
        else:
            distinct_set.append(tempo)
            value += 1
    print(value)


while True:
    command = input("")
    if command == "2":
        sum_sequence()
        m -= 1
    if command == "3":
        distinct_value()
        m -= 1
    else:
        update(command)
        m -= 1
    if m == 0:
        break
