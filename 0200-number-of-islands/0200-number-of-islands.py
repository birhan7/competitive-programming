class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])

        def inbound(row, col):
            return 0 <= row < n and 0 <= col < m and grid[row][col] == "1"
        
        directions = [(0, 1), (1, 0)]

        def dfs(row, col):
            grid[row][col] = "0"
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if inbound(new_row, new_col):
                    dfs(new_row, new_col)
        count = 0      
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count

            
        