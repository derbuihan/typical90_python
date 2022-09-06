import sys


def main():
    input = sys.stdin.readline
    N, Q = map(int, input().split())

    U, V = [], []
    for i in range(N):
        x, y = map(int, input().split())
        u, v = x + y, x - y
        U.append(u)
        V.append(v)

    max_u, min_u = max(U), min(U)
    max_v, min_v = max(V), min(V)

    for i in range(Q):
        q = int(input()) - 1
        u, v = U[q], V[q]
        ans = max(abs(max_u - u), abs(max_v - v),
                  abs(min_u - u), abs(min_v - v))
        print(ans)


if __name__ == '__main__':
    main()
