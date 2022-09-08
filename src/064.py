import sys


def main():
    input = sys.stdin.readline

    N, Q = map(int, input().split())
    A = [0] + list(map(int, input().split())) + [0]

    dA = [A[i + 1] - A[i] for i in range(N + 1)]
    ans = sum(map(abs, dA[1:N]))
    for _ in range(Q):
        l, r, v = map(int, input().split())

        dA[l - 1] += v
        if l - 1 != 0:
            ans -= abs(dA[l - 1] - v)
            ans += abs(dA[l - 1])

        dA[r] -= v
        if r != N:
            ans -= abs(dA[r] + v)
            ans += abs(dA[r])

        print(ans)


if __name__ == '__main__':
    main()
