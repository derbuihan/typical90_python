def main():
    N = int(input())
    S = input()

    status = S[0]
    tmp = 0
    ans = N * (N + 1) // 2
    for s in S:
        if s == status:
            tmp += 1
        else:
            status = s
            ans -= tmp * (tmp + 1) // 2
            tmp = 1
    else:
        ans -= tmp * (tmp + 1) // 2
    print(ans)


if __name__ == '__main__':
    main()
