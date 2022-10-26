import sys


def main():
    read = sys.stdin.read
    N, Q, *XYZW = map(int, read().split())
    X, Y, Z, W = XYZW[::4], XYZW[1::4], XYZW[2::4], XYZW[3::4]

    ans = 1
    for shift in range(60):
        cnt = 0
        for tmp in range(2 ** N):
            for x, y, z, w in zip(X, Y, Z, W):
                x, y, z = x - 1, y - 1, z - 1
                if ((tmp >> x) & 1) \
                        | ((tmp >> y) & 1) \
                        | ((tmp >> z) & 1) \
                        != ((w >> shift) & 1):
                    break
            else:
                cnt += 1
        ans *= cnt
    print(ans % (7 + 10 ** 9))


if __name__ == '__main__':
    main()
