def main():
    N = 4
    c = [
        [10, 2, 5, 2, 5],
        [5, 3, 5, 1, 4],
        [6, 5, 3, 1, 4],
        [6, 3, 7, 9, 4],
    ]

    dp = [float("inf")] * (N + 1)
    dp[0] = 0
    for i in range(N + 1):
        for j in range(i):
            dp[i] = min(dp[i], dp[j] + c[j][i])

    print(dp[N])


main()
