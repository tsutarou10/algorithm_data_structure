def main():
    a = [1, 2, 3, 4, 5, 6]
    N = len(a)
    W, K = map(int, input().split())

    dp = [[float("inf")] * (W + 1) for _ in range(N + 1)]
    dp[0][0] = 0

    for i in range(N):
        for j in range(W + 1):
            if dp[i][j] != float("inf"):
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
            if j - a[i] >= 0 and dp[i][j - a[i]] != float("inf"):
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j - a[i]] + 1)

    if dp[N][W] <= K:
        print("Yes")
    else:
        print("No")


main()
