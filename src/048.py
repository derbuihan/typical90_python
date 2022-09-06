import sys


def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())

    score = []
    for _ in range(N):
        a, b = map(int, input().split())
        score.append(b)
        score.append(a - b)

    score.sort(reverse=True)
    ans = sum(score[:K])
    print(ans)


if __name__ == '__main__':
    main()
