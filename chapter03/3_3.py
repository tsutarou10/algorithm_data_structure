def main():
    A = map(int, input().split())

    min_val = 200000000

    for a in A:
        if a < min_val:
            min_val = a
    print(min_val)


main()
