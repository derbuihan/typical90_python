import sys
from math import inf


def main():
    input = sys.stdin.read
    N, *A = map(int, input().split())

    DP = [[inf for _ in range(2 * N)] for _ in range(2 * N)]
    for l in range(2 * N):
        DP[l][l] = 0
    for l in range(2 * N - 1):
        DP[l][l + 1] = abs(A[l] - A[l + 1])

    for d in range(4, 2 * N + 1, 2):
        for l in range(2 * N):
            r = l + d - 1
            if r >= 2 * N:
                continue
            DP[l][r] = min(DP[l][r], abs(A[l] - A[r]) + DP[l + 1][r - 1])
            for k in range(l + 1, r - 1):
                DP[l][r] = min(DP[l][k] + DP[k + 1][r], DP[l][r])

    print(DP[0][-1])


if __name__ == '__main__':
    main()
