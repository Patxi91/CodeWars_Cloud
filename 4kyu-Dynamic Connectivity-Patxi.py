class DynamicConnectivity(object):
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, p, q):
        rootp = self.find(p)
        rootq = self.find(q)
        if rootp != rootq:
            if self.rank[rootp] < self.rank[rootq]:
                self.parent[rootp] = rootq
            elif self.rank[rootp] > self.rank[rootq]:
                self.parent[rootq] = rootp
            else:
                self.parent[rootq] = rootp
                self.rank[rootp] += 1

    def connected(self, p, q):
        return self.find(p) == self.find(q)
