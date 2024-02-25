def main():
    a = [0, 1, 2, 3, 4, 5]
    W = int(input())

    dp = [[False] * (W + 1) for _ in range(len(a) + 1)]

    dp[0][0] = True
    for i in range(len(a)):
        for j in range(W + 1):
            if dp[i][j]:
                dp[i + 1][j] = True
            if j - a[i] >= 0 and dp[i][j - a[i]]:
                dp[i + 1][j] = True

    if dp[len(a)][W]:
        print("Yes")
    else:
        print("No")


main()
