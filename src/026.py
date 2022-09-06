import sys


def main():
    from collections import deque

    input = sys.stdin.readline
    N = int(input())

    tree = [[] for i in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        a, b = a - 1, b - 1
        tree[a].append(b)
        tree[b].append(a)

    groups = [-1] * N
    q = deque([(0, -1, 0)])
    while q:
        now, pred, color = q.popleft()
        groups[now] = color
        for nxt in tree[now]:
            if nxt == pred:
                continue
            q.append((nxt, now, 1 - color))

    X = [i + 1 for i, g in enumerate(groups) if g == 0]
    Y = [i + 1 for i, g in enumerate(groups) if g == 1]
    if len(X) >= N // 2:
        print(*X[:N // 2])
    else:
        print(*Y[:N // 2])


# TLE
def main2():
    sys.setrecursionlimit(100000)

    input = sys.stdin.readline
    N = int(input())

    tree = [[] for i in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        a, b = a - 1, b - 1
        tree[a].append(b)
        tree[b].append(a)

    def dfs(now, color, groups):
        groups[now] = color
        for nxt in tree[now]:
            if groups[nxt] != -1:
                continue
            dfs(nxt, 1 - color, groups)

    groups = [-1] * N
    dfs(0, 0, groups)

    X = [i + 1 for i, g in enumerate(groups) if g == 0]
    Y = [i + 1 for i, g in enumerate(groups) if g == 1]
    if len(X) >= N // 2:
        print(*X[:N // 2])
    else:
        print(*Y[:N // 2])


if __name__ == '__main__':
    main()
    # main2()
