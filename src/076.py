import sys
from itertools import accumulate


def main():
    input = sys.stdin.read
    N, *A = map(int, input().split())

    S = sum(A)
    if S % 10 != 0:
        print("No")
        return
    S //= 10

    A = A + A
    B = list(accumulate(A))

    l = 0
    for r in range(1, 2 * N):
        s = B[r] - B[l]
        if s == S:
            print("Yes")
            return
        elif s > S:
            l += 1
    print("No")


if __name__ == '__main__':
    main()
