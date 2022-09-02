import sys
from itertools import accumulate


def main():
    input = sys.stdin.readline
    N = int(input())
    A = [0] * N
    B = [0] * N

    for i in range(N):
        c, p = map(int, input().split())
        if c == 1:
            A[i] = p
        else:
            B[i] = p

    accA = [0] + list(accumulate(A))
    accB = [0] + list(accumulate(B))

    Q = int(input())
    for _ in range(Q):
        l, r = map(int, input().split())
        print(accA[r] - accA[l - 1], accB[r] - accB[l - 1])


if __name__ == '__main__':
    main()
