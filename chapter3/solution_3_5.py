from sys import stdin


def main():
    N = int(stdin.readline())
    (*A,) = map(int, stdin.readline().split())

    min_cnt = 1e9 + 10
    for a in A:
        cnt = 0
        while a % 2 == 0:
            a /= 2
            cnt += 1
        if cnt < min_cnt:
            min_cnt = cnt

    print(min_cnt)


main()
