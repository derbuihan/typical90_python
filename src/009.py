import sys
from math import atan2, degrees
from bisect import bisect_left


def main():
    input = sys.stdin.readline
    N = int(input())
    P = [tuple(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        x1, y1 = P[i]

        args = []
        for j in range(N):
            if i == j:
                continue
            x2, y2 = P[j]
            theta = atan2(y2 - y1, x2 - x1)
            args.append(degrees(theta) % 360)
        args.sort()

        for s1 in args:
            s2 = (s1 + 180) % 360
            j = bisect_left(args, s2)
            for k in range(-2, 3):
                jj = min(max(0, j + k), N - 2)
                s3 = args[jj]
                tmp = abs(s1 - s3)
                if tmp > 180:
                    tmp = 360 - tmp
                ans = max(ans, tmp)
    print(ans)


if __name__ == '__main__':
    main()
