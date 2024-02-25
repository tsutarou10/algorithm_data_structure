h = []


def rec(i):
    if i == 0:
        return 0

    res = float("inf")

    res = min(res, rec(i - 1) + abs(h[i] - h[i - 1]))

    if i > 1:
        res = min(res, rec(i - 2) + abs(h[i] - h[i - 2]))

    return res


def main():
    N = 6
    global h
    h = [30, 10, 60, 10, 60, 50]

    rsl = rec(N - 1)
    print(rsl)


main()
