import sys


def main():
    read = sys.stdin.read
    N, K, *AB = map(int, read().split())

    A, B = AB[::2], AB[1::2]
    H, W = max(A), max(B)
    plane = [[0] * (W + 1) for _ in range(H + 1)]
    for a, b in zip(A, B):
        plane[a][b] += 1

    for i in range(H):
        for j in range(W + 1):
            plane[i + 1][j] += plane[i][j]
    for i in range(H + 1):
        for j in range(W):
            plane[i][j + 1] += plane[i][j]

    ans = 0
    for i in range(H + 1):
        for j in range(W + 1):
            ii, jj = max(0, i - K - 1), max(0, j - K - 1)
            tmp = plane[i][j]
            tmp -= plane[ii][j]
            tmp -= plane[i][jj]
            tmp += plane[ii][jj]
            ans = max(ans, tmp)
    print(ans)


if __name__ == '__main__':
    main()
