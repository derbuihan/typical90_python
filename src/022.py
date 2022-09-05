import sys
from math import gcd


def main():
    input = sys.stdin.readline
    A, B, C = map(int, input().split())

    g = gcd(gcd(A, B), C)

    ans = A // g
    ans += B // g
    ans += C // g
    ans -= 3

    print(ans)


if __name__ == '__main__':
    main()
