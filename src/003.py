import sys

sys.setrecursionlimit(100000)


def main():
    read = sys.stdin.read

    N, *ab = map(int, read().split())

    G = [[] for _ in range(N)]
    for i in range(N - 1):
        a, b = ab[2 * i] - 1, ab[2 * i + 1] - 1
        G[a].append(b)
        G[b].append(a)

    def dfs(start):
        visit[start] = True
        for n in G[start]:
            if visit[n]:
                continue
            DP[n] = DP[start] + 1
            dfs(n)

    visit = [False] * N
    DP = [0] * N
    dfs(0)
    edge1 = max(range(N), key=lambda i: DP[i])

    visit = [False] * N
    DP = [0] * N
    dfs(edge1)

    ans = max(DP) + 1
    print(ans)


if __name__ == '__main__':
    main()
