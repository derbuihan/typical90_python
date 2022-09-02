import sys
from bisect import bisect_left
from math import inf


def main():
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    Q = int(input())

    for _ in range(Q):
        b = int(input())
        i = bisect_left(A, b)
        ans = inf
        for j in range(-1, 2):
            ii = min(max(i + j, 0), N - 1)
            ans = min(ans, abs(A[ii] - b))
        print(ans)


if __name__ == '__main__':
    main()
