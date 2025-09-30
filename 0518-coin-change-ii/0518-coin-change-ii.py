class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        memo = {}
        def dp(i,cap):
            if i >= n:
                return 0
            elif cap == 0:
                return 1
            if (i,cap) not in memo:
                include = 0
                exclude = dp(i + 1, cap)
                if cap - coins[i] >= 0:
                    include += dp(i,cap - coins[i])
                memo[(i,cap)] = include + exclude
            return memo[(i,cap)]
        return dp(0,amount)
        
        