import sys
from itertools import permutations
from math import inf


def main():
    input = sys.stdin.readline

    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    M = int(input())
    B = set()
    for _ in range(M):
        x, y = map(lambda i: int(i) - 1, input().split())
        B.add((x, y))
        B.add((y, x))

    ans = inf
    for seq in permutations(range(N)):
        if any([(seq[i], seq[i + 1]) in B for i in range(N - 1)]):
            continue
        tmp = sum([A[seq[i]][i] for i in range(N)])
        ans = min(ans, tmp)

    if ans == inf:
        print(-1)
        return
    print(ans)


if __name__ == '__main__':
    main()
