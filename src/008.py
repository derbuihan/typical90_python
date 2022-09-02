import sys


def main():
    input = sys.stdin.readline
    N = int(input())
    S = input()

    mod = 10 ** 9 + 7

    DP = [0] * 7
    for s in S:
        if s == 'a':
            DP[0] += 1
        elif s == 't':
            DP[1] += DP[0]
        elif s == 'c':
            DP[2] += DP[1]
        elif s == 'o':
            DP[3] += DP[2]
        elif s == 'd':
            DP[4] += DP[3]
        elif s == 'e':
            DP[5] += DP[4]
        elif s == 'r':
            DP[6] += DP[5]
    print(DP[6] % mod)


if __name__ == '__main__':
    main()
