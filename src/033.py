import sys


def main():
    input = sys.stdin.readline
    H, W = map(int, input().split())

    if min(H, W) == 1:
        print(max(H, W))
        return

    ans = (H // 2 + H % 2) * (W // 2 + W % 2)
    print(ans)


if __name__ == '__main__':
    main()
