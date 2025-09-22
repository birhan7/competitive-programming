class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def climb(k):
            if k < 3:
                return k
            if k not in memo:
                memo[k] = climb(k - 1) + climb(k - 2)
            return memo[k]
        return climb(n)
        