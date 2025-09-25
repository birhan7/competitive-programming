class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        n = len(coins)
        memo = {}

        def change(i,cap):
            if cap == 0:
                return 0
            if i == n:
                return float("inf")
            if (i, cap) not in memo:
                include = float("inf")
                if cap >= coins[i]:
                    include = 1 + change(i, cap - coins[i])
                exclude = change(i + 1, cap)
                memo[(i,cap)] = min(include, exclude)
            return memo[(i, cap)]
        ans = change(0,amount)
        return ans if ans != float("inf") else -1



        
        