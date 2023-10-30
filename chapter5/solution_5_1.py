from sys import stdin


def main():
    N = int(stdin.readline())
    A = []
    B = []
    C = []
    for i in range(N):
        a, b, c = map(int, stdin.readline().split())
        A.append(a)
        B.append(b)
        C.append(c)

    dp = [[0] * (3) for _ in range(N)]
    dp[0][0] = A[0]
    dp[0][1] = B[0]
    dp[0][2] = C[0]

    for i in range(1, N):
        dp[i][0] = max(dp[i][0], dp[i - 1][1] + A[i], dp[i - 1][2] + A[i])
        dp[i][1] = max(dp[i][1], dp[i - 1][0] + B[i], dp[i - 1][2] + B[i])
        dp[i][2] = max(dp[i][2], dp[i - 1][0] + C[i], dp[i - 1][1] + C[i])
    print(max(dp[N - 1][0], dp[N - 1][1], dp[N - 1][2]))


main()
