class Edge:
    def __init__(self, to, w):
        self.to = to
        self.w = w


def main():
    N, M = map(int, input().split(' '))

    G = [[] for _ in range(N)]
    for i in range(M):
        a, b, w = input().split(' ')
        a = int(a)
        b = int(b)
        w = float(w)
        G[a].append(Edge(b, w))

    for _from, g in enumerate(G):
        for edge in g:
            print(f'{_from} -> {edge.to}: weight is {edge.w}')


main()
