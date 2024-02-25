from sys import stdin


def func(i, w, a, memo):
    if i == 0:
        return w == 0

    if memo[i][w] is not None:
        return memo[i][w]

    if func(i - 1, w, a, memo):
        memo[i - 1][w] = True
        return memo[i - 1][w]

    if func(i - 1, w - a[i - 1], a, memo):
        memo[i - 1][w - a[i - 1]] = True
        return memo[i - 1][w - a[i - 1]]

    memo[i][w] = False
    return memo[i][w]


def main():
    N, W = map(int, stdin.readline().split())
    (*A,) = map(int, stdin.readline().split())

    memo = [[None for _ in range(W + 1)] for _ in range(N + 1)]
    rsl = "Yes" if func(N, W, A, memo) else "No"
    print(rsl)


main()
