class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l, r = 0, 1
        ans = 0
        while r < n:
            if prices[l] > prices[r]:
                l = r
                r = l + 1
            else:
                ans += prices[r] - prices[l]
                l = r 
                r += 1
        return ans
        