N = 0
h = []
dp = []


def rec(i):
    global N, h, dp
    if dp[i] < float("inf"):
        return dp[i]

    if i == 0:
        return 0

    res = float("inf")
    res = min(res, rec(i - 1) + abs(h[i] - h[i - 1]))
    if i > 1:
        res = min(res, rec(i - 2) + abs(h[i] - h[i - 2]))

    dp[i] = res
    return res


def main():
    global N, h, dp
    N = int(input())
    (*h,) = map(int, input().split())
    dp = [float("inf")] * N
    dp[0] = 0
    rsl = rec(N - 1)
    print(rsl)


main()
