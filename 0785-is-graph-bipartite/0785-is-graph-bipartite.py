class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        m = len(graph)
        color = [-1] * m
        def dfs(vertex):
            queue = deque([vertex])
            while queue:
                curr = queue.popleft()
                for n in graph[curr]:
                    if color[n] == -1:
                        color[n] = 1 - color[curr]
                        queue.append(n)
                    else:
                        if color[n] == color[curr]:
                            return False
            return True
        for i in range(m):
            if color[i] == -1:
                color[i] = 1
                if not dfs(i):
                    return False
        return True
                    
        

        