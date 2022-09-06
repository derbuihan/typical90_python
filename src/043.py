from collections import deque
from math import inf


def main():
    H, W = map(int, input().split())
    rs, cs = map(int, input().split())
    rt, ct = map(int, input().split())

    S = ["#" * (W + 2)]
    S += ["#" + input() + "#" for _ in range(H)]
    S += ["#" * (W + 2)]

    def pos_num(y, x, d):
        n = 4 * (W + 2) * y + 4 * x + d
        return n

    def num_pos(n):
        d = n % 4
        x = ((n - d) // 4) % (W + 2)
        y = (n - 4 * x - d) // (4 * (W + 2))
        return y, x, d

    space = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visit = [False] * (H + 2) * (W + 2) * 4
    dist = [inf] * (H + 2) * (W + 2) * 4
    for d in range(4):
        dist[pos_num(rs, cs, d)] = 0

    q = deque([(0, pos_num(rs, cs, d)) for d in range(4)])
    while q:
        c, now = q.pop()
        if visit[now]:
            continue
        visit[now] = True

        y, x, d = num_pos(now)
        dy, dx = space[d]
        ny, nx = y + dy, x + dx
        nxt = pos_num(ny, nx, d)
        if S[ny][nx] != "#" and dist[nxt] > c:
            q.append((c, nxt))
            dist[nxt] = c

        for nd in range(4):
            nxt = pos_num(y, x, nd)
            if dist[nxt] > c + 1:
                q.appendleft((c + 1, nxt))
                dist[nxt] = c + 1

    ans = min([dist[pos_num(rt, ct, d)] for d in range(4)])
    print(ans)


if __name__ == '__main__':
    main()
