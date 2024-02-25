from sys import stdin


def main():
    (*A,) = map(int, stdin.readline().split())

    min1 = A[0] if A[0] < A[1] else A[1]
    min2 = A[0] if A[0] >= A[1] else A[1]

    for i in range(2, len(A)):
        if A[i] < min1:
            min2 = min1
            min1 = A[i]
            continue
        if A[i] == min1:
            min1 = min2 = A[i]
            continue
        if A[i] < min2:
            min2 = A[i]

    print(min2)


main()
