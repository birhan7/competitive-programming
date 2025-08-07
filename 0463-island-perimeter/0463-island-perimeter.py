class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row_length, col_length = len(grid), len(grid[0])
        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False for _ in range(col_length)] for _ in range(row_length)]

        def inbound(row, col):
            return 0 <= row < row_length and 0 <= col < col_length and grid[row][col] == 1

        def dfs(row, col):
            perimeter = 0
            visited[row][col] = True

            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change

                if not inbound(new_row, new_col):
                    perimeter += 1
                if inbound(new_row, new_col) and not visited[new_row][new_col]:
                        perimeter += dfs(new_row, new_col)
            return perimeter 

        for i in range(row_length):
            for j in range(col_length):
                if grid[i][j] == 1:
                    return dfs(i, j)
        
      
                    

        