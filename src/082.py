def main():
    L, R = map(int, input().split())

    def f(n):
        return n * (n + 1) // 2

    def count(n):
        ret = 0
        i = 0
        while i + 1 <= len(str(n)):
            ret += (i + 1) * (f(10 ** (i + 1) - 1) - f(10 ** i - 1))
            i += 1
        ret += i * (f(n) - f(10 ** i - 1))
        return ret

    ans = count(R) - count(L - 1)
    print(ans % (10 ** 9 + 7))


if __name__ == '__main__':
    main()
