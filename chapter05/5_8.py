def main():
    S = "logistic"
    T = "algorithm"

    dp = [[float("inf")] * (len(T) + 1) for _ in range(len(S) + 1)]

    dp[0][0] = 0

    for i in range(len(S) + 1):
        for j in range(len(T) + 1):
            if i - 1 >= 0 and j - 1 >= 0:
                # modify
                if S[i - 1] == T[j - 1]:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
                else:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + 1)

            # remove
            if i - 1 >= 0:
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)

            # insert
            if j - 1 >= 0:
                dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)

    print(dp[len(S)][len(T)])


main()
