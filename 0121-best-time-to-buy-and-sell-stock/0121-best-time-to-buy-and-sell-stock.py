class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l, r = 0, 1
        max_profit = 0
        while r < n:
            price_left, price_right = prices[l], prices[r]
            if price_left > price_right:
                l = r
            else:
                max_profit = max(max_profit, price_right - price_left)
                r += 1
        return max_profit
        
        