class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {0: 0, 1: 1, 2: 1}
        def tri(k):
            if k not in memo:
                memo[k] = tri(k - 1) + tri(k - 2) + tri(k - 3)
            return memo[k]
        return tri(n)
        