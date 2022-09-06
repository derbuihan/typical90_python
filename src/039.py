import sys

sys.setrecursionlimit(100000)


def main():
    input = sys.stdin.readline

    N = int(input())

    tree = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(lambda x: int(x) - 1, input().split())
        tree[a].append(b)
        tree[b].append(a)

    def dfs(tree, now, pred, count):
        for nxt in tree[now]:
            if nxt == pred:
                continue
            dfs(tree, nxt, now, count)
            count[now] += count[nxt]

    count = [1] * N
    dfs(tree, 0, -1, count)

    ans = sum([c * (N - c) for c in count])
    print(ans)


if __name__ == '__main__':
    main()
