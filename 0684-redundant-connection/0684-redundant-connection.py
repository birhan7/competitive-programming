class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = { i:i for i in range(n+1)}
        def union(u,v):
            pu, pv = parent[u], parent[v]
            if pu != pv:
                parent[pu] = pv
        def find(u):
            if parent[u] == u:
                return u
            parent[u] = find(parent[u])
            return parent[u]
        def is_connected(u,v):
            return find(u) == find(v)
        
        for u, v in edges:
            if is_connected(u,v):
                return [u,v]
            else:
                union(u,v)
        