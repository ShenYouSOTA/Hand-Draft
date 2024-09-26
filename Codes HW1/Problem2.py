def main():
    constraint = input("").split()
    n = int(constraint[0])
    q = int(constraint[1])

    permutation = list(map(int, input("").split()))
    left_piece = list(map(int, input("").split()))
    right_piece = list(map(int, input("").split()))

    pos = {val: idx + 1 for idx, val in enumerate(permutation)}
    b = [{'head': 0, 'tail': 0, 'vis': False} for _ in range(n + 1)]

    for i in range(q):
        lp = pos[left_piece[i]]
        rp = pos[right_piece[i]]

        if lp >= rp:
            print(0)
            return

        if not b[lp]['vis'] and not b[rp]['vis']:
            if any(b[j]['vis'] for j in range(lp, rp)):
                print(0)
                return
            for j in range(lp, rp + 1):
                b[j]['vis'] = True
            b[lp]['tail'], b[rp]['head'] = rp, lp
        elif b[lp]['tail'] and not b[rp]['vis']:
            j = rp
            while j > lp:
                if b[j]['vis']:
                    if b[j]['head'] != lp:
                        print(0)
                        return
                    b[j]['head'] = 0
                    break
                b[j]['vis'] = True
                j -= 1
            b[lp]['tail'], b[rp]['head'] = rp, lp

    if not all(b[i]['vis'] for i in range(1, n + 1)):
        print(0)
    else:
        print(1)


if __name__ == "__main__":
    main()

