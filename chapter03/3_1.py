def main():
    _ = int(input())
    A = map(int, input().split())
    v = int(input())

    for a in A:
        if a == v:
            print("Yes")
            return
    print("No")


main()
