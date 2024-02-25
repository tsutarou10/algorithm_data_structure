from sys import stdin
import bisect


def main():
    N = int(stdin.readline())
    (*A,) = map(int, stdin.readline().split())
    (*B,) = map(int, stdin.readline().split())
    (*C,) = map(int, stdin.readline().split())

    A.sort()
    B.sort()
    C.sort()
    rsl = 0
    for b in B:
        idx_a = bisect.bisect_left(A, b)
        num_a = idx_a
        if A[idx_a - 1] == b:
            num_a -= 1
        idx_c = bisect.bisect_right(C, b)
        num_c = idx_c
        rsl += (num_a) * (N - num_c)

    print(rsl)


main()
