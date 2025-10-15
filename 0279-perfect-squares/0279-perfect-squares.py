class Solution:
    def numSquares(self, n: int) -> int:
        p_squares = []
        for i in range(1, n + 1):
            x = sqrt(i)
            if x == int(x):
                p_squares.append(i)
        memo = {}
        def dfs(need):
            if need == 0:
                return 0
            if need not in memo:
                temp = float('inf')
                for s in p_squares:
                    if need - s >= 0:
                        temp = min(dfs(need - s) + 1, temp) 
                memo[need] = temp
            return memo[need]
        return dfs(n)

        