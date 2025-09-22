class Solution:
    def fib(self, n: int) -> int:
        memo = {0: 0, 1: 1}
        if n not in memo:
            memo[n] = self.fib(n - 1) + self.fib(n - 2)
        return memo[n]
        