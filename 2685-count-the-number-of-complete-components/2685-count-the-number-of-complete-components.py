class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [False for _ in range(n)]
        degree = [0 for _ in range(n)]
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1

        def bfs(queue):
            node_count = 1
            visited1 = set()
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        node_count += 1
                        visited[neighbor] = True
                        visited1.add(neighbor)
                        queue.append(neighbor)
            deg = node_count - 1
            for val in visited1:
                if not degree[val] == deg:
                    return False
            return True

        components = 0
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                queue = deque([i])
                temp = bfs(queue)
                if temp:
                    components += 1

        return components
        