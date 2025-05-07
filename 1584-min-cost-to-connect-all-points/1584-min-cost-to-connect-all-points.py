class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        w_g = []
        n = len(points)
        points.sort()
        for i in range(n):
            cost = float("inf")
            for j in range(n):
                if i != j:
                    dis = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    w_g.append([dis,i,j])
        w_g.sort(reverse=True)
        total = 0
        uf = UnionFind()
        while w_g:
            cost, u, v = w_g.pop()
            if not uf.connected(u,v):
                uf.union(u,v)
                total += cost
        return total

class UnionFind:
    def __init__(self):
        self.parent = defaultdict(int)
        self.size = {}

    def find(self,u):
        if u not in self.parent:
            self.parent[u] = u
            self.size[u] = 1
        if self.parent[u] == u:
            return u
        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self,u, v):
        p1, p2 = self.find(u), self.find(v)
        s1, s2 = self.size[u], self.size[v]
        if p1 != p2:
            if s1 > s2:
                self.parent[p2] = p1
                self.size[p1] += self.size[p2]
            else:
                self.parent[p1] = p2
                self.size[p2] += self.size[p1]

    def connected(self,u, v):
        return self.find(u) == self.find(v)
        
        