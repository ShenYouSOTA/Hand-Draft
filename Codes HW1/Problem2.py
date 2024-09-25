constraint = input("")
n = int(constraint[0])
q = int(constraint[1])
access = False
coverage = False

permutation = input("").split()
left_piece = input("").split()
right_piece = input("").split()


def fail_test(L, R):
    try:
        index_L = permutation.index(L)
        index_R = permutation.index(R)
        if index_L >= index_R:
            return True
        return False
    except ValueError:
        return True


for i in range(1, q + 1):
    pivot = -i
    left, right = left_piece[pivot], right_piece[pivot]
    if fail_test(left, right):
        break
