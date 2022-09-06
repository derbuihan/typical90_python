def main():
    N = int(input())

    history = set()
    for i in range(N):
        S = input()
        if S in history:
            continue
        print(i + 1)
        history.add(S)


if __name__ == '__main__':
    main()
