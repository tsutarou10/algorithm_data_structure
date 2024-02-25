from sys import stdin


def main():
    N = int(stdin.readline())
    (*h,) = map(int, stdin.readline().split())

    cost = [float("inf")] * (N)

    cost[0] = 0

    for i in range(1, N):
        if i == 1:
            cost[i] = abs(h[i] - h[i - 1])
        else:
            cost[i] = min(
                cost[i - 1] + abs(h[i] - h[i - 1]), cost[i - 2] + abs(h[i] - h[i - 2])
            )

    print(cost[N - 1])


main()
