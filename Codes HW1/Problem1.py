raw_data: str = input("")
lines = raw_data.splitlines()
basic_info = lines[0].split()
raw_series = lines[1].split()

"""
n: The length of the sequence.
m: The number of operations. 
P: The divisor in modulo operation.
"""

n, m, P = int(basic_info[0]), int(basic_info[1]), int(basic_info[2])

series: list = [int(num) for num in raw_series]


def update(factor: str) -> None:
    factor = factor.split()
    k = int(factor[1])
    x = int(factor[2])
    y = int(factor[3])
    c = int(factor[4])
    temp = x ** 2 + k * y + 5 * x
    series[k - 1] = (temp % P) * c


def sum_sequence() -> None:
    total = sum(series)
    print(total)


def distinct_value() -> None:
    value = 0
    distinct_set = set()
    for i in range(n):
        tempo = series[i]
        if tempo in distinct_set:
            tempo = tempo * (-1)
            if tempo in distinct_set:
                continue
            else:
                distinct_set.add(tempo)
                value += tempo
        else:
            distinct_set.add(tempo)
            value += tempo
    print(value)


for j in range(2, n):
    temp = lines[j]
    if temp == "2":
        sum_sequence()
    if temp == "3":
        distinct_value()
    else:
        update(temp)
