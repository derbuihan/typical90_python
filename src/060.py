import sys
from math import inf
from bisect import bisect_left


def main():
    read = sys.stdin.read
    N, *A = map(int, read().split())

    def LIS(xs):
        DP = [inf] * N
        ret = [0] * N
        max_ret = 0
        for i in range(N):
            x = xs[i]
            j = bisect_left(DP, x)
            DP[j] = x
            max_ret = max(max_ret, j)
            ret[i] = max_ret + 1
        return ret

    X = LIS(A)
    Y = LIS(A[::-1])
    ans = max([x + y - 1 for x, y in zip(X, Y[::-1])])
    print(ans)


if __name__ == '__main__':
    main()
