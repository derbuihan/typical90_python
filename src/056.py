import sys


def main():
    read = sys.stdin.read
    N, S, *AB = map(int, read().split())
    A, B = AB[::2], AB[1::2]

    DP = [set() for _ in range(N + 1)]
    DP[0].add(0)

    for i, (a, b) in enumerate(zip(A, B)):
        for x in DP[i]:
            if x + a <= S:
                DP[i + 1].add(x + a)
            if x + b <= S:
                DP[i + 1].add(x + b)

    if S not in DP[N]:
        print("Impossible")
        return

    ans = ""
    for i in range(N - 1, -1, -1):
        a, b = A[i], B[i]
        if S - a in DP[i]:
            ans = "A" + ans
            S -= a
        else:
            ans = "B" + ans
            S -= b
    print(ans)


if __name__ == '__main__':
    main()
