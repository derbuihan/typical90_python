import sys


def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    mod = 7 + 10 ** 9

    ans = 1
    for i in range(N):
        if i > 1:
            ans *= pow(K - 2, N - 2, mod)
            break
        ans *= K - i
    print(ans % mod)


if __name__ == '__main__':
    main()
