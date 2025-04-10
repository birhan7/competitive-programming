class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        def inbound(x,y):
            return (0 <= x < len(grid)) and (0 <= y < len(grid[0]))
        def dfs(row,col):
            area = 0
            if grid[row][col] == 0:
                return 0
            area += 1
            grid[row][col] = 0
            for dx, dy in directions:
                new_row, new_col = dx + row, dy + col
                if inbound(new_row, new_col):
                    area += dfs(new_row,new_col) 
            return area
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ans = max(ans,dfs(i,j))
        return ans
                
