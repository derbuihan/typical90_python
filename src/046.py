import sys


def main():
    read = sys.stdin.read
    N, *ABC = map(int, read().split())

    A, B, C = ABC[:N], ABC[N:2 * N], ABC[2 * N:]

    count_A, count_B, count_C = [0] * 46, [0] * 46, [0] * 46
    for i in range(N):
        count_A[A[i] % 46] += 1
        count_B[B[i] % 46] += 1
        count_C[C[i] % 46] += 1

    ans = 0
    for i in range(46):
        for j in range(46):
            for k in range(46):
                if (i + k + j) % 46 == 0:
                    ans += count_A[i] * count_B[j] * count_C[k]
    print(ans)


if __name__ == '__main__':
    main()
