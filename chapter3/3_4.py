def main():
    A = map(int, input().split())
    B = map(int, input().split())
    K = int(input())

    min_val = 20000000
    for a in A:
        for b in B:
            if a + b >= K and a + b < min_val:
                min_val = a + b
    print(min_val)


main()
