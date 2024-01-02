from sys import stdin


def main():
    N = int(stdin.readline())
    H = []
    S = []
    for i in range(N):
        h, s = map(int, stdin.readline().split())
        H.append(h)
        S.append(s)

    M = 0
    for i in range(N):
        M = max(M, H[i] + N * S[i])

    left = 0
    right = M
    while right - left > 1:
        mid = int((left + right) / 2)

        ok = True
        t = [0] * N
        for i in range(N):
            if mid < H[i]:
                ok = False
            else:
                t[i] = (mid - H[i]) / S[i]

        t.sort()
        for i in range(N):
            if t[i] < i:
                ok = False

        if ok:
            right = mid
        else:
            left = mid

    print(right)


main()
