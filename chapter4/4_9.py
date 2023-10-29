from sys import stdin

A = []


def func(i, w):
    if i == 0:
        return w == 0

    return func(i - 1, w) or func(i - 1, w - A[i - 1])


def main():
    global A
    N, W = map(int, stdin.readline().split())
    (*A,) = map(int, stdin.readline().split())

    rsl = "Yes" if func(N, W) else "No"
    print(rsl)


main()
