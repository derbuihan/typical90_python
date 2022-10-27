import sys
from itertools import product


def main():
    read = sys.stdin.read
    N, *DCS = map(int, read().split())
    D, C, S = DCS[::3], DCS[1::3], DCS[2::3]

    rewards = []
    for bits in product([0, 1], repeat=N):
        works = [(D[i], C[i], S[i]) for i in range(N) if bits[i] == 1]
        works.sort()

        day = 0
        reward = 0
        for d, c, s in works:
            day += c
            if day > d:
                break
            reward += s
        else:
            rewards.append(reward)

    print(max(rewards))


def main2():
    read = sys.stdin.read
    N, *DCS = map(int, read().split())
    D, C, S = DCS[::3], DCS[1::3], DCS[2::3]
    works = [(D[i], C[i], S[i]) for i in range(N)]
    works.sort()

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
