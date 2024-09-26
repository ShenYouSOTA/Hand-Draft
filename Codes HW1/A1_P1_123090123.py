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
distinct_value = 0
distinct_numbers = {}
for i in series:
    i = abs(i)
    if i in distinct_numbers:
        if i == 0:
            continue
        distinct_numbers[i] += 1
    else:
        distinct_numbers[i] = 1


for num in distinct_numbers:
    if distinct_numbers[num] >= 2:
        distinct_value += 2
    else:
        distinct_value += 1  # distinct_numbers[num]


def update(factor: str) -> None:
    global summation, distinct_value
    factor = factor.split()
    k = int(factor[1])
    x = int(factor[2])
    y = int(factor[3])
    c = int(factor[4])
    previous = series[k - 1]
    current = (x ** 2 + k * y + 5 * x) % P * c
    series[k - 1] = current
    summation = summation - previous + current
    previous = abs(previous)
    current = abs(current)
    if previous == 0:
        if distinct_numbers[previous] >= 2:
            distinct_numbers[previous] -= 1
        else:
            distinct_value -= 1
            del distinct_numbers[previous]
    else:
        if distinct_numbers[previous] == 1:
            del distinct_numbers[previous]
            distinct_value -= 1
        elif distinct_numbers[previous] == 2:
            distinct_numbers[previous] -= 1
            distinct_value -= 1
        else:
            distinct_numbers[previous] -= 1
    if current in distinct_numbers:
        if current != 0 and distinct_numbers[current] < 2:
            distinct_value += 1
        distinct_numbers[current] += 1
    else:
        distinct_numbers[current] = 1
        distinct_value += 1


while 0 < m:
    line = input("")
    if line == "2":
        print(summation)
    elif line == "3":
        print(distinct_value)
    else:
        update(line)
    m -= 1
