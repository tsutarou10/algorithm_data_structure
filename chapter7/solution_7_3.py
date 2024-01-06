def main():
    N = int(input())
    W = []
    for _ in range(N):
        a, b = map(int, input().split())
        W.append((a, b))
    W.sort(key=lambda x: (x[1], x[0]))

    rsl = 0
    for i in range(N):
        rsl += W[i][0]
        if rsl > W[i][1]:
            print("No")
            return
    print("Yes")


main()
