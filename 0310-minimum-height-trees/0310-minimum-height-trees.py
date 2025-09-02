class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        if n == 2:
            return edges[0]
        graph = [[] for _ in range(n)]
        degree = [0] * (n)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1

        one_degree = []
        for i in range(n):
            if degree[i] == 1:
                one_degree.append(i)
        queue = deque(one_degree)
        ans = set()
        visited = set(one_degree)
        while queue:
            ans.clear()
            for _ in range(len(queue)):
                node = queue.popleft()
                ans.add(node)
                if degree[node] != 1:
                    degree[node] = float("inf")
                for nbr in graph[node]:
                    if nbr not in visited:
                        degree[nbr] -= 1
                        if degree[nbr] == 1:
                            queue.append(nbr)
                            visited.add(nbr)

        return list(ans)


        