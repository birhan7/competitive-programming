class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = [[[],[]] for _ in range(n)]
        for a, b in redEdges:
            graph[a][0].append(b)
        for a, b in blueEdges:
            graph[a][1].append(b)

        queue = deque([(0,0),(0,1)])
        visited = set([(0,0),(0,1)])
        ans = [-1 for _ in range(n)]
        length = 0
        while queue:
            for _ in range(len(queue)):
                node, color = queue.popleft()
                if ans[node] == -1:
                    ans[node] = length

                alternative = 1 - color
                for neighbor in graph[node][alternative]:
                    if (neighbor,alternative) not in visited:
                        visited.add((neighbor,alternative))
                        queue.append((neighbor,alternative))
            length += 1
        return ans
        