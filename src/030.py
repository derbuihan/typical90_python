import sys


def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())

    factor = [0] * (N + 1)
    for p in range(2, N + 1):
        if factor[p] > 0:
            continue
        for i in range(p, N + 1, p):
            factor[i] += 1

    ans = 0
    for c in factor:
        if c >= K:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
