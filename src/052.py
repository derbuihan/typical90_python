import sys


def main():
    input = sys.stdin.readline
    N = int(input())

    ans = 1
    for _ in range(N):
        ans *= sum(map(int, input().split()))
        ans %= 10 ** 9 + 7

    print(ans)


if __name__ == '__main__':
    main()
