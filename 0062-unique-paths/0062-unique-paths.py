class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def move(i, j):
            if i >=m or j >= n:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            if (i, j) not in memo:
                memo[(i, j)] = move(i + 1, j) + move(i, j + 1)
            return memo[(i, j)]
        return move(0,0)
        