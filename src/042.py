import sys


def main():
    input = sys.stdin.readline
    K = int(input())

    if K % 9 != 0:
        print(0)
        return

    DP = [0] * (K + 1)
    DP[0] = 1
    for i in range(K + 1):
        for j in range(1, min(i + 1, 10)):
            DP[i] += DP[i - j]
        DP[i] %= 10 ** 9 + 7

    print(DP[-1])


if __name__ == '__main__':
    main()
