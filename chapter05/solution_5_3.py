from sys import stdin


def main():
    N = int(stdin.readline())
    (*p,) = map(int, stdin.readline().split())

    dp = [[False] * 10010 for _ in range(N + 1)]
    dp[0][0] = True

    for i in range(N):
        for j in range(10010):
            if dp[i][j]:
                dp[i + 1][j] = True
            if j - p[i] >= 0 and dp[i][j - p[i]]:
                dp[i + 1][j] = True

    s = set()
    for j in range(10010):
        if j in s:
            continue
        if dp[N][j]:
            s.add(j)

    print(len(s))


main()
