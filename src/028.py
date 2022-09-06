import sys


def main():
    input = sys.stdin.readline
    N = int(input())

    M = 1001
    plane = [[0] * M for _ in range(M)]
    for _ in range(N):
        lx, ly, rx, ry = map(int, input().split())
        plane[lx][ly] += 1
        plane[rx][ry] += 1
        plane[lx][ry] -= 1
        plane[rx][ly] -= 1

    for i in range(M):
        for j in range(M - 1):
            plane[i][j + 1] += plane[i][j]

    for i in range(M - 1):
        for j in range(M):
            plane[i + 1][j] += plane[i][j]

    A = [0] * (N + 1)
    for i in range(M):
        for j in range(M):
            k = plane[i][j]
            A[k] += 1

    print(*A[1:], sep="\n")


if __name__ == '__main__':
    main()
