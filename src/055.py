import sys


def main():
    read = sys.stdin.read

    N, P, Q, *A = map(int, read().split())

    ans = 0
    for i in range(N - 4):
        a = A[i] % P
        for j in range(i + 1, N - 3):
            b = a * A[j] % P
            for k in range(j + 1, N - 2):
                c = b * A[k] % P
                for l in range(k + 1, N - 1):
                    d = c * A[l] % P
                    for m in range(l + 1, N):
                        e = d * A[m] % P
                        if e == Q:
                            ans += 1
    print(ans)


# TLE
def main2():
    from itertools import combinations

    read = sys.stdin.read

    N, P, Q, *A = map(int, read().split())

    ans = 0
    for i, j, k, l, m in combinations(range(N), 5):
        a = A[i] % P
        b = a * A[j] % P
        c = b * A[k] % P
        d = c * A[l] % P
        e = d * A[m] % P
        if e == Q:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
    # main2()
