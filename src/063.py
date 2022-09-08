import sys
from itertools import product
from collections import defaultdict


def main():
    input = sys.stdin.readline

    H, W = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(H)]

    ans = 0
    for bits in product([0, 1], repeat=H):
        if sum(bits) == 0:
            continue
        xss = [P[j] for j in range(H) if bits[j] == 1]

        count = defaultdict(int)
        count[0] = 0
        for i in range(W):
            x = xss[0][i]
            if all([x == xs[i] for xs in xss]):
                count[x] += 1

        ans = max(ans, max(count.values()) * sum(bits))
    print(ans)


if __name__ == '__main__':
    main()
