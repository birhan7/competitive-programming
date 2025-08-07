class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        perimeter = 0

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
                return 1
            if grid[row][col] == -1:
                return 0
            
            grid[row][col] = -1
            return (dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1))
            
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    perimeter +=  dfs(i, j)
        return perimeter
        
      
                    

        