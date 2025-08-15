class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def inbound(row,col):
            return 0 <= row < rows and 0 <= col < cols

        def bfs(row,col):
            nonlocal curr
            if grid[row][col] == 1:
                return -1
            directions = [(-1,0),(1,0),(-1,1),(-1,-1),(1,1),(0,1),(0,-1),(1,-1)]
            queue = deque([(row,col)])
            visited = set((row,col))
            distance = 0
            curr = (row,col)
            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    curr = (r,c)
                    if r == rows - 1 and c  == cols - 1:
                        return distance + 1
                    for dr, dc in directions:
                        new_row, new_col = r + dr, c + dc
                        if inbound(new_row,new_col) and grid[new_row][new_col] == 0 and (new_row,new_col) not in visited:
                            visited.add((new_row,new_col))
                            queue.append((new_row,new_col))
                distance += 1
            return distance
        curr = (0,0)
        ans = bfs(*curr)
        if curr != (rows - 1, cols - 1):
            return -1
        return ans


        