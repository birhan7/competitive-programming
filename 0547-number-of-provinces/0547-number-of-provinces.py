class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1:
                    graph[i+1].append(j+1)
                else:
                    graph[i+1].extend([])
        def dfs(vertex,visited):
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    dfs(neighbor,visited)
        
        count = 0
        visited = set()
        for node in graph:
            if node not in visited:
                count += 1
                dfs(node,visited)
        return count