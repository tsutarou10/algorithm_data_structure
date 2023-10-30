from sys import stdin


def main():
    N = int(stdin.readline())
    (*h,) = map(int, stdin.readline().split())

    dp = [float("inf")] * N

    dp[0] = 0

    for i in range(N):
        if i + 1 < N:
            dp[i + 1] = min(dp[i + 1], dp[i] + abs(h[i] - h[i + 1]))
        if i + 2 < N:
            dp[i + 2] = min(dp[i + 2], dp[i] + abs(h[i] - h[i + 2]))

    print(dp[N - 1])


main()
