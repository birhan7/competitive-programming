class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for i in range(len(manager)):
            if manager[i] != -1:
                graph[manager[i]].append(i)
        def dfs(vertex,graph):
            time = 0
            for neighbor in graph[vertex]:
                time = max(time,dfs(neighbor,graph))
            return informTime[vertex] + time
        return dfs(headID,graph)

        