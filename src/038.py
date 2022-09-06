import sys
from math import gcd


def main():
    input = sys.stdin.readline
    A, B = map(int, input().split())

    g = gcd(A, B)
    ans = A * B // g

    if ans > 10 ** 18:
        print("Large")
        return

    print(ans)


if __name__ == '__main__':
    main()
