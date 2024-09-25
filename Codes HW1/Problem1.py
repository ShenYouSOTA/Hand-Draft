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
    factor = factor.split()
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
    distinct_set = set()
    for num in series:
        if num not in distinct_set and -num not in distinct_set:
            distinct_set.add(num)
    print(len(distinct_set))


while 0 < m:
    command = input("")
    if command == "2":
        sum_sequence()
    elif command == "3":
        distinct_value()
    else:
        update(command)
    m -= 1
