class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans = [[] for _ in range(n)]
        graph = [[] for _ in range(n)]
        indegree = [0 for _ in range(n)]
        zero_indegree = set()
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
            if indegree[u] == 0:
                zero_indegree.add(u)
            if v in zero_indegree:
                zero_indegree.remove(v)
        print(zero_indegree)
        queue = deque(list(zero_indegree))
        while queue:
            node = queue.popleft()
            for nbr in graph[node]:
                indegree[nbr] -= 1
                res = [*ans[nbr],*ans[node],node]
                print(res)
                ans[nbr] = list(set(res))
                if indegree[nbr] == 0:
                    queue.append(nbr)
        for i in range(n):
            ans[i].sort()
        return ans
        