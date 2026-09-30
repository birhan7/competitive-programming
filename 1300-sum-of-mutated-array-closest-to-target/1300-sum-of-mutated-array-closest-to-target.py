class Solution:
    def findBestValue(self, arr: list[int], target: int) -> int:
        if target >= sum(arr):
            return max(arr)
        l, r = 0, target
        min_num, min_diff = target, target
        while l <= r:
            m = (l + r) // 2
            total = self.check(arr, m)
            if total == target:
                return m
            elif total > target:
                r = m - 1
            else:
                l = m + 1
            
            diff = abs(target - total)
            if min_diff > diff:
                min_num = m
            elif min_diff == diff:
                min_num = min(min_num, m)
            min_diff = min(min_diff, diff)

        return min_num

        
    def check(self, arr, value):
        total = 0
        for num in arr:
            total += min(num, value)
        return total
        
        
        





        