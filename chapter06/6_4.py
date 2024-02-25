from sys import stdin
import bisect

INF = 20000000


def main():
    N, K = map(int, stdin.readline().split())
    (*a,) = map(int, stdin.readline().split())
    (*b,) = map(int, stdin.readline().split())

    min_value = INF
    b.sort()
    b.append(INF)

    for i in range(0, N):
        key = bisect.bisect_left(b, K - a[i])
        val = b[key]
        if a[i] + val < min_value:
            min_value = a[i] + val

    print(min_value)


main()
