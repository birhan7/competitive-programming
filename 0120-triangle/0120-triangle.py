class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        length = len(triangle)
        memo = {}
        def dfs(i, j):
            if i == length:
                return 0
            min_path = float('inf')
            if i == 0 and j == 0:
                return triangle[i][j] + min(dfs(i + 1, j), dfs(i + 1, j + 1))
            if (i, j) not in memo:
                min_path = triangle[i][j] + min(dfs(i + 1, j), dfs(i + 1, j + 1))
                memo[(i, j)] = min_path
            return memo[(i, j)]
        return dfs(0, 0)
        