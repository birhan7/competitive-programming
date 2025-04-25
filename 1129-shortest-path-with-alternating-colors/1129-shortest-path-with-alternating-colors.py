class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        col = row = n
        ans = []
        graph = defaultdict(list)
        for u, v in redEdges:
            graph[u].append([v,"red"])
        for u, v in blueEdges:
            graph[u].append([v,"blue"])
        

        def bfs(vertex):
            queue = deque([[0,"blue"],[0,"red"]])
            visited = [[[False,False] for _ in range(n)] for _ in range(col)]
            step = 0
            while queue:
                length = len(queue)
                for _ in range(length):
                    curr, color = queue.popleft()
                    if curr == vertex:
                        return step
                    for neighbor in graph[curr]:
                        nbr_visited = False
                        nbr_clr = neighbor[1]
                        temp = visited[curr][neighbor[0]]
                        if nbr_clr == "red":
                            nbr_visited = temp[0]
                        else:
                            nbr_visited = temp[1]

                        if color != nbr_clr and not nbr_visited:
                            if color == "blue":
                                temp[0] = True
                            else:
                                temp[1] = True
                            queue.append(neighbor)
                
                step += 1
            return -1

        for i in range(n):
            ans.append(bfs(i))
        return ans

        