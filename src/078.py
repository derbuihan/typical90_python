import sys
from collections import defaultdict


def main():
    read = sys.stdin.read
    N, M, *ab = map(int, read().split())

    counts = defaultdict(int)
    it = iter(ab)
    for a, b in zip(it, it):
        a, b = sorted([a, b])
        counts[b] += 1

    ans = 0
    for val in counts.values():
        if val == 1:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
