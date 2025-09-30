class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n= len(matrix)
        if n == 1:
            return matrix[0][0]
        memo = [[10**9] * n for _ in range(n)]
        for j in range(n):
            memo[0][j] = matrix[0][j]

        
        
        for row in range(1, n):
            for col in range(n):
                memo[row][col] = min(memo[row][col], memo[row - 1][col])
                if col + 1 < n:
                    memo[row][col] = min(memo[row][col],memo[row - 1][col + 1])
                if col - 1 >= 0:
                    memo[row][col] = min(memo[row][col], memo[row - 1][col - 1])
                memo[row][col] += matrix[row][col]
        return min(*memo[n - 1])

        