def read_input():
    start = input("").split()
    n = int(start[0])
    q = int(start[1])

    permutation = list(map(int, input("").split()))
    left_pieces = list(map(int, input("").split()))
    right_pieces = list(map(int, input("").split()))

    return n, q, permutation, left_pieces, right_pieces


def initialize(n):
    position_array = [0] * (n + 1)
    index_position = [0] * (n + 1)
    block_info = [{'head': 0, 'tail': 0, 'visited': False} for _ in range(n + 1)]
    return position_array, index_position, block_info


def fill_position_array(n, permutation, position_array, index_position):
    for i in range(1, n + 1):
        position_array[i] = permutation[i - 1]
        index_position[position_array[i]] = i


def handle_head_to_tail(L, R, block):
    temp = L
    while True:
        if block[temp]['visited']:
            if block[temp]['tail'] != R:
                return False
            block[temp]['tail'] = 0
            break
        block[temp]['visited'] = True
        temp += 1
    block[L]['tail'], block[R]['head'] = R, L
    return True


def handle_tail_to_head(L, R, block):
    temp = R
    while True:
        if block[temp]['visited']:
            if block[temp]['head'] != L:
                return False
            block[temp]['head'] = 0
            break
        block[temp]['visited'] = True
        temp -= 1
    block[L]['tail'], block[R]['head'] = R, L
    return True


def both_blocks_unvisited(L, R, block):
    return not block[L]['visited'] and not block[R]['visited']


def handle_non_visited_blocks(L, R, block):
    for j in range(L, R + 1):
        if block[j]['visited']:
            return False
        block[j]['visited'] = True
    block[L]['tail'], block[R]['head'] = R, L
    return True


def process_visited_blocks(L, R, block):
    if block[L]['tail'] and not block[R]['visited']:
        return handle_tail_to_head(L, R, block)
    elif block[R]['head'] and not block[L]['visited']:
        return handle_head_to_tail(L, R, block)
    elif block[L]['tail'] and block[R]['head']:
        if block[L]['tail'] + 1 != block[R]['head']:
            return False
        block[L]['tail'], block[R]['head'] = R, L
        return True
    return False


def all_blocks_connected(block, n):
    return (block[1]['tail'] == n and
            block[n]['head'] == 1 and
            all(block[i]['visited'] for i in range(1, n + 1)))


def process_queries(n, q, permutation, left_pieces, right_pieces):
    position_array, index_position, block = initialize(n)
    fill_position_array(n, permutation, position_array, index_position)

    for query_index in range(q, 0, -1):
        L = index_position[left_pieces[query_index - 1]]
        R = index_position[right_pieces[query_index - 1]]

        if L >= R:
            return 0

        if both_blocks_unvisited(L, R, block):
            if not handle_non_visited_blocks(L, R, block):
                return 0
        else:
            if not process_visited_blocks(L, R, block):
                return 0

    if not all_blocks_connected(block, n):
        return 0

    return 1


def main():
    n, q, permutation, left_pieces, right_pieces = read_input()
    result = process_queries(n, q, permutation, left_pieces, right_pieces)
    print(result)


if __name__ == "__main__":
    main()
