import sys

sys.setrecursionlimit(100000)


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]


def main():
    input = sys.stdin.readline

    H, W = map(int, input().split())
    Q = int(input())

    def pos_num(y, x):
        return y * W + x

    tree = UnionFind(H * W)
    track = [False] * (H * W)
    ds = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    for i in range(Q):
        q = input()
        if q[0] == '1':
            _, r, c = map(lambda x: int(x) - 1, q.split())
            x = pos_num(r, c)
            track[x] = True
            for dy, dx in ds:
                rr = sorted([0, r + dy, H - 1])[1]
                cc = sorted([0, c + dx, W - 1])[1]
                y = rr * W + cc
                if track[y]:
                    tree.union(x, y)

        elif q[0] == '2':
            _, ra, ca, rb, cb = map(lambda x: int(x) - 1, q.split())
            xa, xb = pos_num(ra, ca), pos_num(rb, cb)
            if track[xa] and track[xb] and tree.find(xa) == tree.find(xb):
                print("Yes")
                continue
            print("No")


if __name__ == '__main__':
    main()
