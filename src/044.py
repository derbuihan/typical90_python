import sys


def main():
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))

    shift = 0
    for _ in range(Q):
        t, x, y = map(int, input().split())
        if t == 1:
            x += shift - 1
            x %= N
            y += shift - 1
            y %= N
            A[x], A[y] = A[y], A[x]

        elif t == 2:
            shift -= 1
            shift %= N

        elif t == 3:
            x += shift - 1
            x %= N
            print(A[x])


if __name__ == '__main__':
    main()
