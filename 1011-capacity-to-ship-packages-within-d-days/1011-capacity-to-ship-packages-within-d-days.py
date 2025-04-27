class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def validate(capacity):
            total_sum = 0
            total_days = 1
            for weight in weights:
                total_sum += weight
                if total_sum > capacity:
                    total_days += 1
                    total_sum = weight
                if total_days > days:
                    return False
            return True

        low, high = max(weights),sum(weights)
        while low <= high:
            mid = (low + high)//2
            if validate(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low

        