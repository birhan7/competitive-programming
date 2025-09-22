class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        def fibonacci(k):
            if k is 1 or k is 0:
                return k
            if k not in memo:
                memo[k] = self.fib(k - 1) + self.fib(k - 2)
            return memo[k]
        return fibonacci(n)
        