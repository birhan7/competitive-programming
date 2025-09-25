class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
        n, m = len(grid), len(grid[0]) 
        def inbound(row, col):
            return 0 <= row < n and 0 <= col < m
        def calc(i, j):
            if i == n - 1 and j == m - 1:
                return grid[i][j]
            if (i, j) not in memo:
                temp = float("inf")
                if inbound(i + 1, j):
                    temp = min(temp, calc(i + 1, j)) 
                if inbound(i, j + 1):
                    temp = min(calc(i, j + 1), temp)
                memo[(i, j)] = grid[i][j] + temp
            return memo[(i, j)]
        return calc(0,0)
        