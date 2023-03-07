class UnionFind:
    def __init__(self, n):
        self.p = [i for i in range(n + 1)]
        self.rank = [1 for _ in range(n + 1)]

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])

        return self.p[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        if self.rank[px] > self.rank[py]:
            self.p[py] = px
            self.rank[px] += self.rank[py]
        else:
            self.p[px] = py
            self.rank[py] += self.rank[px]
