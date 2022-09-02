import sys
from math import inf
from heapq import heapify, heappush, heappop


def main():
    input = sys.stdin.readline

    N, M = map(int, input().split())

    G = [[] for i in range(N)]

    for i in range(M):
        a, b, c = map(int, input().split())
        a, b = a - 1, b - 1
        G[a].append((b, c))
        G[b].append((a, c))

    def dijkstra(start, G, N):
        q = [(0, start, -1)]
        heapify(q)
        dist = [inf] * N
        dist[start] = 0
        while q:
            now_dist, now, pred = heappop(q)
            for nxt, nxt_cost in G[now]:
                if nxt == pred:
                    continue

                nxt_dist = now_dist + nxt_cost
                if nxt_dist >= dist[nxt]:
                    continue

                heappush(q, (nxt_dist, nxt, now))
                dist[nxt] = nxt_dist
        return dist

    dist1 = dijkstra(0, G, N)
    dist2 = dijkstra(N - 1, G, N)

    for x, y in zip(dist1, dist2):
        print(x + y)


# TLE
def main2():
    from scipy import sparse
    import numpy as np

    read = sys.stdin.read
    N, M, *abc = map(int, read().split())
    a, b, c = abc[::3], abc[1::3], abc[2::3]
    a = list(map(lambda x: x - 1, a))
    b = list(map(lambda x: x - 1, b))

    G = sparse.coo_matrix((c, (a, b)), shape=(N, N)).tocsr()
    dist = sparse.csgraph.shortest_path(G, directed=False, indices=[0, N - 1])
    ans = np.sum(dist, axis=0, dtype=np.int_)
    print(*ans, sep='\n')


if __name__ == '__main__':
    main()
    # main2()
