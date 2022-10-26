import sys


def main():
    read = sys.stdin.read
    N, Q, *XYZW = map(int, read().split())
    X, Y, Z, W = XYZW[::4], XYZW[1::4], XYZW[2::4], XYZW[3::4]
    XYZ = [(x - 1, y - 1, z - 1) for x, y, z in zip(X, Y, Z)]
    mod = 10 ** 9 + 7

    def func(tmp, shift):
        for (x, y, z), w in zip(XYZ, W):
            a_x = (tmp >> x) & 1
            a_y = (tmp >> y) & 1
            a_z = (tmp >> z) & 1
            w_s = (w >> shift) & 1
            if a_x | a_y | a_z != w_s:
                return False
        return True

    ans = 1
    for shift in range(60):
        ans *= sum([func(tmp, shift) for tmp in range(2 ** N)])
        ans %= mod
    print(ans)


if __name__ == '__main__':
    main()
