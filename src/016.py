import sys
from math import inf


def main():
    input = sys.stdin.readline
    N = int(input())
    A, B, C = map(int, input().split())

    M = 9999

    ans = inf
    for i in range(0, M):
        if i * A > N:
            break
        for j in range(0, M - i):
            if i * A + j * B > N:
                break
            k = (N - A * i - B * j) // C
            if A * i + B * j + C * k == N:
                ans = min(ans, i + j + k)
    print(ans)


if __name__ == '__main__':
    main()
