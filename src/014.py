import sys


def main():
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    ans = sum([abs(a - b) for a, b in zip(A, B)])
    print(ans)


if __name__ == '__main__':
    main()
