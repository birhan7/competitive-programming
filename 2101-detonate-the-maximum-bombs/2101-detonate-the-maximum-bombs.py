class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        length = len(bombs)
        graph = [[] for _ in range(length)]
        for i in range(length):
            x1, y1, r1 = bombs[i]
            for j in range(length):
                if i != j:
                    x2, y2, r2 = bombs[j]
                    if sqrt(pow(abs(x2 - x1),2) + pow(abs(y2 - y1),2)) <= r1:
                        graph[i].append(j)
                    if sqrt(pow(abs(x2 - x1),2) + pow(abs(y2 - y1),2)) <= r2:
                        graph[j].append(i)

        def dfs(vertex,visited):
            total = 0
            visited.add(vertex)
            for neighbor in graph[vertex]:
                count = 0
                if neighbor not in visited:
                    count = max(count,dfs(neighbor,visited))
                total += count
            return total + 1

        ans = 0
        for i in range(length):
           ans = max(ans,dfs(i,set()))
        return ans

                    
        