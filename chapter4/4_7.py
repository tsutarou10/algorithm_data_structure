def main():
    N = 50
    F = [0, 1]

    for i in range(2, N):
        F.append(F[i - 1] + F[i - 2])
        print(f"{i} items: {F[i]}")


main()
