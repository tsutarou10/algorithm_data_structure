from sys import stdin


def main():
    (*A,) = map(int, stdin.readline().split())
    V = int(stdin.readline())

    cnt = 0
    for a in A:
        if a == V:
            cnt += 1
    print(cnt)


main()
