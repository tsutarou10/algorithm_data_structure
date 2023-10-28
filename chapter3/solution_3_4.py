from sys import stdin


def main():
    (*A,) = map(int, stdin.readline().split())

    min_val = max_val = A[0]

    for a in A:
        if min_val > a:
            min_val = a
        if max_val < a:
            max_val = a
    print(max_val - min_val)


main()
