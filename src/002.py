import sys
from itertools import product


def main():
    input = sys.stdin.readline
    N = int(input())

    if N % 2 != 0:
        return

    kakko = {-1: ')', 1: '('}
    ans = []
    for bits in product([-1, 1], repeat=N):
        if sum(bits) != 0:
            continue
        tmp = 0
        for b in bits:
            tmp += b
            if tmp < 0:
                break
        else:
            test = "".join([kakko[b] for b in bits])
            ans.append(test)

    for a in sorted(ans):
        print(a)


if __name__ == '__main__':
    main()
