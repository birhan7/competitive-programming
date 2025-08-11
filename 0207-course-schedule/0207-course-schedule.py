class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        WHITE, GREY, BLACK = -1, 0, 1
        colors = {k:WHITE  for k in range(numCourses)}
        for ai, bi in prerequisites:
            graph[bi].append(ai)
        can_finish = True
        def dfs(vertex):
            nonlocal can_finish
            if not can_finish:
                return False

            colors[vertex] = GREY
            for neighbor in graph[vertex]:
                if colors[neighbor] == GREY:
                    can_finish = False
                elif colors[neighbor] == WHITE:
                    dfs(neighbor)
            colors[vertex] = BLACK

        for key in range(numCourses):
            if colors[key] == WHITE:
                dfs(key)
        return can_finish

        