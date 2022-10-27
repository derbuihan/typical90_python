import sys


def main():
    read = sys.stdin.read
    N, *DCS = map(int, read().split())
    D, C, S = DCS[::3], DCS[1::3], DCS[2::3]
    works = sorted(zip(D, C, S))

    ans = 0
    for bits in range(2 ** N):
        day = 0
        reward = 0
        for j in range(N):
            if (bits >> j) & 1:
                d, c, s = works[j]
                day += c
                if day > d:
                    break
                reward += s
        else:
            ans = max(reward, ans)

    print(ans)


def main2():
    read = sys.stdin.read
    N, *DCS = map(int, read().split())
    D, C, S = DCS[::3], DCS[1::3], DCS[2::3]
    works = sorted(zip(D, C, S))

    DP = [[0] * 5001 for i in range(N + 1)]

    for i in range(N):
        d, c, s = works[i]
        for j in range(5001):
            DP[i + 1][j] = max(DP[i + 1][j], DP[i][j])
            if j + c <= d:
                DP[i + 1][j + c] = max(DP[i + 1][j + c], DP[i][j] + s)

    print(max(DP[N]))


if __name__ == '__main__':
    # main()
    main2()
