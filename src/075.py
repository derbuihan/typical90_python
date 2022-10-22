from collections import Counter


def main():
    N = int(input())

    factors = []
    i = 2
    while i * i <= N:
        if N % i == 0:
            N //= i
            factors.append(i)
        else:
            i += 1
    else:
        factors.append(N)

    counts = Counter(factors)
    s = sum([val for key, val in counts.items()])
    for i in range(s):
        if 2 ** (i - 1) < s <= 2 ** i:
            print(i)
            return


if __name__ == '__main__':
    main()
