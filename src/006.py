from collections import deque


def main():
    N, K = map(int, input().split())
    S = input()

    q = deque()
    ans = ""
    for i in range(N):
        s = S[i]
        while q and s < q[-1]:
            q.pop()
        q.append(s)
        if i >= N - K:
            ans += q.popleft()

    print(ans)


if __name__ == '__main__':
    main()
