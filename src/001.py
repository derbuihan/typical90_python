import sys


def main():
    read = sys.stdin.read

    N, L, K, *A = map(int, read().split())
    B = [A[0]] + [A[i + 1] - A[i] for i in range(N - 1)] + [L - A[N - 1]]

    def sep(B, leng):
        n = len(B)
        tmp = 0
        cnt = 0
        for i in range(n):
            b = B[i]
            tmp += b
            if tmp > leng:
                cnt += 1
                tmp = 0
        return cnt

    l, r = 0, L
    while l + 1 != r:
        m = (l + r) // 2
        if sep(B, m) > K:
            l = m
        else:
            r = m
    print(r)


if __name__ == '__main__':
    main()
