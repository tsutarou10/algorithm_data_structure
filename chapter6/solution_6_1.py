from sys import stdin
import bisect
import copy


def main():
    N = int(stdin.readline())
    (*A,) = map(int, stdin.readline().split())

    copied_A = copy.deepcopy(A)

    A.sort()

    rsl = []
    for a in copied_A:
        rsl.append(bisect.bisect_left(A, a))

    print(" ".join(map(str, rsl)))


main()
