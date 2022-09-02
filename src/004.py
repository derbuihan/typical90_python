import sys


def main():
    import numpy as np

    read = sys.stdin.read
    H, W, *arr = map(int, read().split())

    A = np.array(arr, dtype=np.int_).reshape((H, W))

    xs = np.sum(A, axis=0).reshape((1, W))
    B = np.tile(xs, (H, 1))

    ys = np.sum(A, axis=1).reshape((H, 1))
    C = np.tile(ys, (1, W))

    X = B + C - A
    for ans in X:
        print(*ans)


def main2():
    read = sys.stdin.read
    H, W, *arr = map(int, read().split())

    A = [arr[W * i: W * (i + 1)] for i in range(H)]

    xs = [0] * W
    ys = [0] * H
    for i in range(H):
        for j in range(W):
            xs[j] += A[i][j]
            ys[i] += A[i][j]

    for i in range(H):
        ans = []
        for j in range(W):
            tmp = xs[j] + ys[i] - A[i][j]
            ans.append(tmp)
        print(*ans)


if __name__ == '__main__':
    main()
    # main2()
