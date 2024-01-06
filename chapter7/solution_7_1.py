import bisect


def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    rsl = 0
    for j in range(N):
        if A[rsl] < B[j]:
            rsl += 1

    print(rsl)


main()
