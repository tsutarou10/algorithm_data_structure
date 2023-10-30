from sys import stdin


def main():
    N, W = map(int, stdin.readline().split())
    w_l, v_l = [], []
    for _ in range(N):
        w, v = map(int, stdin.readline().split())
        w_l.append(w)
        v_l.append(v)

    dp = [[0] * (W + 1) for _ in range(N + 1)]

    for i in range(N):
        for w in range(W + 1):
            if w - w_l[i] >= 0:
                dp[i + 1][w] = max(dp[i + 1][w], dp[i][w - w_l[i]] + v_l[i])
            dp[i + 1][w] = max(dp[i + 1][w], dp[i][w])

    print(dp[N][W])


main()
