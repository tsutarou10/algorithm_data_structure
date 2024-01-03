import bisect


def main():
    N, M = map(int, input().split())
    p = [0] + [int(input()) for _ in range(N)]

    X = set()
    for p1 in p:
        for p2 in p:
            X.add(p1 + p2)

    X = list(X)
    X.sort()

    rsl = 0

    for x in X:
        idx = max(0, bisect.bisect_left(X, M - x) - 1)
        tmp_rsl = x + X[idx]
        if tmp_rsl > M:
            continue
        rsl = max(rsl, tmp_rsl)

    print(rsl)


main()
