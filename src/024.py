import sys


def main():
    read = sys.stdin.read
    N, K, *AB = map(int, read().split())
    A, B = AB[:N], AB[N:]

    count = sum(map(lambda a, b: abs(a - b), A, B))

    if count > K or count % 2 != K % 2:
        print("No")
        return
    print("Yes")


if __name__ == '__main__':
    main()
