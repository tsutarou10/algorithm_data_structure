from sys import stdin


def main():
    N, W = map(int, stdin.readline().split())
    (*A,) = map(int, stdin.readline().split())

    for bit in range(1 << N):
        sum_val = 0
        for i in range(N):
            if bit & (1 << i):
                sum_val += A[i]
        if sum_val == W:
            print("Yes")
            return
    print("No")


main()
