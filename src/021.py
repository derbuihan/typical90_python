import sys

sys.setrecursionlimit(100000)


def main():
    input = sys.stdin.read
    N, M, *AB = map(int, input().split())
    AB = list(map(lambda x: x - 1, AB))
    A, B = AB[::2], AB[1::2]

    link = [[] for _ in range(N)]
    relink = [[] for _ in range(N)]
    for a, b in zip(A, B):
        link[a].append(b)
        relink[b].append(a)

    def dfs(start, G, visit, track):
        visit[start] = True
        for n in G[start]:
            if visit[n]:
                continue
            dfs(n, G, visit, track)
        track.append(start)

    visit = [False] * N
    track = []
    for i in range(N):
        if visit[i]:
            continue
        dfs(i, link, visit, track)
    track.reverse()

    ans = 0
    visit = [False] * N
    for i in track:
        if visit[i]:
            continue
        track = []
        dfs(i, relink, visit, track)
        ans += len(track) * (len(track) - 1) // 2
    print(ans)


if __name__ == '__main__':
    main()
