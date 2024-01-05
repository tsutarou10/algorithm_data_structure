import bisect

INF = 1 << 60


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    B.sort()

    left = 0
    right = INF

    while right - left > 1:
        x = (left + right) // 2
        cnt = 0
        for i in range(N):
            cnt += bisect.bisect_right(B, x // A[i])
        if cnt >= K:
            right = x
        else:
            left = x

    print(right)


main()
