import sys
from collections import defaultdict


def main():
    input = sys.stdin.read
    N, K, *A = map(int, input().split())

    count = defaultdict(int)
    ans = K
    l = 0
    for r in range(N):
        count[A[r]] += 1
        while len(count) > K:
            count[A[l]] -= 1
            if count[A[l]] == 0:
                del count[A[l]]
            l += 1
        ans = max(ans, r - l + 1)
    print(ans)


if __name__ == '__main__':
    main()
