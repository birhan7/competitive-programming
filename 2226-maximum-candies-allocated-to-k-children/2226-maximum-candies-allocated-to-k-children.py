class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def check(size):
            count = 0
            for candy in candies:
                val = candy // size
                if val:
                    count += val
            return count >= k

        low, high = 1, max(candies)
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                low = mid + 1
            else:
                high = mid - 1
        return high 