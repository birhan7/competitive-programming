class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = [0] * n
        for u,v in edges:
            indegree[v] += 1
        count = 0
        for i in range(len(indegree)):
            if indegree[i] == 0:
                champion = i
                count += 1
        return champion if count == 1 else -1