import sys
from itertools import combinations
from bisect import bisect_right
from collections import defaultdict


def main():
    read = sys.stdin.read
    N, K, P, *A = map(int, read().split())

    def count(B):
        lenB = len(B)
        countB = defaultdict(list)
        for i in range(lenB + 1):
            countBi = countB[i]
            for comb in combinations(range(lenB), i):
                s = sum([B[c] for c in list(comb)])
                countBi.append(s)
            countBi.sort()
        return countB

    m = N // 2
    X, Y = A[:m], A[m:]
    countX, countY = count(X), count(Y)

    ans = 0
    for i in range(0, K + 1):
        j = K - i
        for x in countX[i]:
            ans += bisect_right(countY[j], P - x)
    print(ans)


if __name__ == '__main__':
    main()
