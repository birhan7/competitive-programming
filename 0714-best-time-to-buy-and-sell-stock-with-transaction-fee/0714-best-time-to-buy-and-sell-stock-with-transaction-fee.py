class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        length = len(prices)
        memo = {}
        def dfs(i, sell):
            if i >= length:
                return 0
            if (i, sell) not in memo:
                include, exclude = 0, 0
                if not sell:
                    include = dfs(i + 1, True) - prices[i]
                    exclude = dfs(i + 1, sell)
                else:
                    include = dfs(i + 1, False) + prices[i] - fee
                    exclude = dfs(i + 1, sell)
                memo[(i, sell)] = max(include, exclude)
            return memo[(i, sell)]
        return dfs(0, False)
        