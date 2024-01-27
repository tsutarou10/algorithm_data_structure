def main():
    N, M = map(int, input().split(' '))

    G = [[] for _ in range(N)]

    for _ in range(M):
        a, b = map(int, input().split(' '))
        G[a].append(b)
        G[b].append(a)

    print(G)


main()
