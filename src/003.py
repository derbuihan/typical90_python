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

    def dfs(G, start, dist, visit):
        visit[start] = True
        for n in G[start]:
            if visit[n]:
                continue
            dist[n] = dist[start] + 1
            dfs(G, n, dist, visit)

    dist1 = [0] * N
    visit1 = [False] * N
    dfs(G, 0, dist1, visit1)
    edge1 = max(range(N), key=lambda i: dist1[i])

    dist2 = [0] * N
    visit2 = [False] * N
    dfs(G, edge1, dist2, visit2)

    ans = max(dist2) + 1
    print(ans)


if __name__ == '__main__':
    main()
