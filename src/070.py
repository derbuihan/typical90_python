import sys


def main():
    input = sys.stdin.read
    N, *XY = map(int, input().split())
    xs, ys = XY[::2], XY[1::2]
    xs.sort()
    ys.sort()

    x_m, y_m = xs[N // 2], ys[N // 2]
    ans = sum([abs(x_m - x) for x in xs])
    ans += sum([abs(y_m - y) for y in ys])
    print(ans)


if __name__ == '__main__':
    main()
