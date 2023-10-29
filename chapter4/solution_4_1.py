from sys import stdin


def tribo(n):
    if n <= 1:
        return 0
    if n == 2:
        return 1

    return tribo(n - 1) + tribo(n - 2) + tribo(n - 3)


def main():
    N = int(stdin.readline())
    rsl = tribo(N - 1)
    print(f"T_{N-1}: {rsl}")


main()
