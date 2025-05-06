class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind()
        n = len(equations)
        for eq in equations:
            if eq[1:3] == "==":
                uf.union(eq[0],eq[3])
        for eq in equations:
            if eq[1:3] == "!=":
                if uf.connected(eq[0],eq[3]):
                    return False      
        return True

class UnionFind:
    def __init__(self):
        self.parent = defaultdict(str)
        self.size = defaultdict(int)

    def find(self,u):
        if u not in self.parent:
            self.parent[u] = u
        if self.parent[u] == u:
            return u
        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self,u,v):
        pu, pv = self.find(u), self.find(v)
        su, sv = self.size[pu], self.size[pv]
        if pu != pv:
            if su > sv:
                self.parent[pv] = pu
                self.size[pu] += self.size[pv]
            else:
                self.parent[pu] = pv
                self.size[pv] += self.size[pu]

    def connected(self,u,v):
        return self.find(u) == self.find(v)

        