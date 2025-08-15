class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(-1,0),(1,0),(-1,1),(-1,-1),(1,1),(0,1),(0,-1),(1,-1)]
        n = len(grid)

        def inbound(row,col):
            return 0 <= row < rows and 0 <= col < cols

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        queue = deque([(0,0,1)])
        visited = set((0,0))
        while queue:
            r, c, distance = queue.popleft()
            if r == n - 1 and c == n - 1:
                return distance
            for dr, dc in directions:
                new_row, new_col = r + dr, c + dc
                if inbound(new_row,new_col) and (new_row,new_col) not in visited and grid[new_row][new_col] == 0:
                    visited.add((new_row,new_col))
                    queue.append((new_row,new_col,distance + 1))
        return -1

        
        