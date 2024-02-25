class UnionFind:
    def __init__(self, n):
        # the number of the parent vertex for each vertex
        self.par = [-1 for i in range(n)]
        # the size of the vertexes that are in root-tree
        self.siz = [1 for i in range(n)]

    def root(self, x):
        if self.par[x] == -1:
            return x  # if x is root the function returns x
        self.par[x] = self.root(self.par[x])
        return self.par[x]

    def is_same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return False

        # union by size
        if self.siz[x] < self.siz[y]:
            x, y = y, x

        self.par[y] = x
        self.siz[x] += self.siz[y]
        return True

    def size(self, x):
        return self.siz[self.root(x)]


def main():
    uf = UnionFind(7)  # {0}, {1}, {2}, ..., {6}

    uf.unite(1, 2)  # {0}, {1, 2}, {3}, ..., {6}
    uf.unite(2, 3)  # {0}, {1, 2, 3}, {4}, ..., {6}
    uf.unite(5, 6)  # {0}, {1, 2, 3}, {4}, {5, 6}

    print(uf.is_same(1, 3))  # True
    print(uf.is_same(2, 5))  # False

    uf.unite(1, 6)  # {0}, {1, 2, 3, 5, 6}, {4}

    print(uf.is_same(2, 5))  # True


main()
