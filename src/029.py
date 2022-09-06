import sys


# TLE
def main():
    input = sys.stdin.readline
    W, N = map(int, input().split())

    line = [0] * W
    for _ in range(N):
        l, r = map(lambda x: int(x) - 1, input().split())

        m = max(line[l: r + 1])
        for i in range(l, r + 1):
            line[i] = m + 1
        print(m + 1)


def main2():
    class LazySegTree:
        def __init__(self, init_val, segfunc, ide_ele):
            n = len(init_val)
            self.segfunc = segfunc
            self.ide_ele = ide_ele
            self.num = 1 << (n - 1).bit_length()
            self.data = [ide_ele] * 2 * self.num
            self.lazy = [None] * 2 * self.num
            for i in range(n):
                self.data[self.num + i] = init_val[i]
            for i in range(self.num - 1, 0, -1):
                self.data[i] = self.segfunc(self.data[2 * i],
                                            self.data[2 * i + 1])

        def gindex(self, l, r):
            l += self.num
            r += self.num
            lm = l >> (l & -l).bit_length()
            rm = r >> (r & -r).bit_length()

            while r > l:
                if l <= lm:
                    yield l
                if r <= rm:
                    yield r
                r >>= 1
                l >>= 1
            while l:
                yield l
                l >>= 1

        def propagates(self, *ids):
            for i in reversed(ids):
                v = self.lazy[i]
                if v is None:
                    continue
                self.lazy[2 * i] = v
                self.lazy[2 * i + 1] = v
                self.data[2 * i] = v
                self.data[2 * i + 1] = v
                self.lazy[i] = None

        def update(self, l, r, x):
            *ids, = self.gindex(l, r)
            self.propagates(*ids)
            l += self.num
            r += self.num
            while l < r:
                if l & 1:
                    self.lazy[l] = x
                    self.data[l] = x
                    l += 1
                if r & 1:
                    self.lazy[r - 1] = x
                    self.data[r - 1] = x
                r >>= 1
                l >>= 1
            for i in ids:
                self.data[i] = self.segfunc(self.data[2 * i],
                                            self.data[2 * i + 1])

        def query(self, l, r):
            *ids, = self.gindex(l, r)
            self.propagates(*ids)

            res = self.ide_ele

            l += self.num
            r += self.num
            while l < r:
                if l & 1:
                    res = self.segfunc(res, self.data[l])
                    l += 1
                if r & 1:
                    res = self.segfunc(res, self.data[r - 1])
                l >>= 1
                r >>= 1
            return res

    input = sys.stdin.readline
    W, N = map(int, input().split())

    init_val = [0] * W
    segfunc = lambda x, y: max(x, y)
    ide_ele = 0
    tree = LazySegTree(init_val, segfunc, ide_ele)

    for _ in range(N):
        l, r = map(lambda x: int(x) - 1, input().split())

        m = tree.query(l, r + 1)
        tree.update(l, r + 1, m + 1)
        print(m + 1)


if __name__ == '__main__':
    # main()
    main2()
