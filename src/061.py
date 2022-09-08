import sys
from collections import deque


def main():
    input = sys.stdin.readline

    Q = int(input())

    deck = deque()
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            deck.appendleft(x)
        elif t == 2:
            deck.append(x)
        else:
            print(deck[x - 1])


if __name__ == '__main__':
    main()
