import sys


def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())

    def func(x):
        y = sum(map(int, str(x)))
        return (x + y) % (10 ** 5)

    memo = {}
    while K > 0:
        memo[N] = K
        N = func(N)
        K -= 1
        if N in memo:
            K %= (memo[N] - K)
    print(N)


if __name__ == '__main__':
    main()
