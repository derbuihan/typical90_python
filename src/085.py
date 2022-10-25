def main():
    K = int(input())

    divisors = []
    i = 1
    while i * i < K:
        if K % i == 0:
            divisors.append(i)
            divisors.append(K // i)
        i += 1
    else:
        if i * i == K:
            divisors.append(i)
    divisors.sort()

    ans = 0
    n = len(divisors)
    for i in range(n):
        a = divisors[i]
        for j in range(i, n):
            b = divisors[j]
            c = K // (a * b)
            if a <= b <= c and a * b * c == K:
                ans += 1
    print(ans)


if __name__ == '__main__':
    main()
