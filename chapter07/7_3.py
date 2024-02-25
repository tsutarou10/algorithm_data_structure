def main():
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    A = reversed(A)
    B = reversed(B)
    rsl = 0
    for a, b in zip(A, B):
        p = (rsl + a) // b
        q = (rsl + a) % b
        rsl += b * (p + (q != 0)) - (rsl + a)

    print(int(rsl))


main()
