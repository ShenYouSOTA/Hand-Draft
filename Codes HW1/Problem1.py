basic_info = input("").split()
raw_series = input("").split()
"""
n: The length of the sequence.
m: The number of operations. 
P: The divisor in modulo operation.
"""
# Initialize
n, m, P = int(basic_info[0]), int(basic_info[1]), int(basic_info[2])
series: list = [int(num) for num in raw_series]
summation = sum(series)
distinct_set = set()
for i in series:
    distinct_set.add(i)
    if series.count(i) > 1:
        distinct_set.add(-i)
distinct_value = len(distinct_set)


def detect_withdraw(num: int) -> None:
    global distinct_set
    if num == 0:
        if series.count(num) == 0:
            distinct_set.remove(num)
    else:
        a = series.count(num)
        b = series.count(-num)
        if a + b < 2:
            if a == 0:
                distinct_set.remove(num)
            else:
                distinct_set.remove(-num)


def detect_entry(num: int) -> None:
    global distinct_set
    a = series.count(num)
    b = series.count(-num)
    if (a+b) < 2 and b == 0:
        num = -num
    distinct_set.add(num)


def update(factor: str) -> None:
    global distinct_value, summation
    factor = factor.split()
    k = int(factor[1])
    x = int(factor[2])
    y = int(factor[3])
    c = int(factor[4])
    temp = x ** 2 + k * y + 5 * x
    current = (temp % P) * c

    previous = series.pop(k-1)
    detect_withdraw(previous)
    detect_entry(current)
    series.insert(k - 1, current)
    summation = summation - previous + current
    distinct_value = len(distinct_set)


def sum_sequence() -> None:
    print(summation)


def count_distinct() -> None:
    print(distinct_value)


while 0 < m:
    command = input("")
    if command == "2":
        sum_sequence()
    elif command == "3":
        count_distinct()
    else:
        update(command)
    m -= 1
