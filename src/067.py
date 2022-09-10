import sys


def main():
    input = sys.stdin.readline
    N, K = input().split()

    def func(xs):
        n = sum([x * (8 ** i) for i, x in enumerate(xs[::-1])])
        ys = []
        while n != 0:
            y = n % 9
            if y == 8:
                y = 5
            ys.append(y)
            n //= 9
        ys.reverse()
        return ys

    xs = list(map(int, N))
    K = int(K)
    for i in range(K):
        xs = func(xs)

    ans = sum([x * (10 ** i) for i, x in enumerate(xs[::-1])])
    print(ans)


if __name__ == '__main__':
    main()
