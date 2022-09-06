import sys


def main():
    input = sys.stdin.readline
    N, L = map(int, input().split())

    DP = [0] * (N + 1)
    DP[0] = 1
    for i in range(N):
        DP[i + 1] += DP[i]
        if i + L <= N:
            DP[i + L] += DP[i]

    print(DP[-1] % (10 ** 9 + 7))


if __name__ == '__main__':
    main()
