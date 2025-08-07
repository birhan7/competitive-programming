class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row_length, col_length = len(grid), len(grid[0])
        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False for _ in range(col_length)] for _ in range(row_length)]

        def inbound(row, col):
            return 0 <= row < row_length and 0 <= col < col_length and grid[row][col] == "1"

        def dfs(row, col):
            visited[row][col] = True

            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change

                if inbound(new_row, new_col) and not visited[new_row][new_col]:
                    dfs(new_row, new_col)
        
        conn_component = 0
        for i in range(row_length):
            for j in range(col_length):
                if grid[i][j] == "1" and not visited[i][j]:
                    dfs(i, j)
                    conn_component += 1
        return conn_component
            
        