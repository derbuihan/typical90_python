import sys
import numpy as np
from numpy import cos, sin, pi, arccos, degrees
from numpy.linalg import norm


def main():
    input = sys.stdin.readline
    T = int(input())
    L, X, Y = map(int, input().split())

    O = np.array([X, Y, 0])

    def pos(e):
        x = 0
        y = - sin(2 * pi * e / T) * (L / 2)
        z = (1 - cos(2 * pi * e / T)) * (L / 2)
        return np.array([x, y, z])

    Q = int(input())
    for _ in range(Q):
        e = int(input())
        if e == 0:
            print(0)
            continue

        p1 = pos(e)
        p2 = pos(e)
        p2[2] = 0

        inn = (p1 - O) @ (p2 - O)
        inn /= norm(p1 - O) * norm(p2 - O)
        theta = arccos(inn)
        ans = degrees(theta)
        print(ans)


if __name__ == '__main__':
    main()
