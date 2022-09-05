import sys


def main():
    input = sys.stdin.readline
    a, b, c = map(int, input().split())

    if a < c ** b:
        print("Yes")
        return
    print("No")


if __name__ == '__main__':
    main()
