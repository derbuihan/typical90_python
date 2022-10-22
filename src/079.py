import sys


def main():
    read = sys.stdin.read
    H, W, *AB = map(int, read().split())
    A, B = AB[:H * W], AB[H * W:]

    ans = 0
    for x in range(H - 1):
        for y in range(W - 1):
            i = x * W + y
            c = B[i] - A[i]
            for a, b in [(0, 0), (0, 1), (1, 0), (1, 1)]:
                i = (x + a) * W + (y + b)
                A[i] += c
            ans += abs(c)

    if A != B:
        print("No")
        return
    print("Yes")
    print(ans)


if __name__ == '__main__':
    main()
