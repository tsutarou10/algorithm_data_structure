INF = 200000000


def main():
    N, M = map(int, input().split())
    (*a,) = map(int, input().split())

    a.sort()

    left = 0
    right = INF
    while right - left > 1:
        x = int((left + right) / 2)
        cnt = 1
        prev = 0
        for i in range(N):
            if a[i] - a[prev] >= x:
                cnt += 1
                prev = i

        if cnt >= M:
            left = x
        else:
            right = x

    print(left)


main()
