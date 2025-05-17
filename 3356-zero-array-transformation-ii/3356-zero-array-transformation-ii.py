class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def check(k):
            prefix = [0] * len(nums)
            for i in range(k):
                l, r, val = queries[i]
                prefix[l] += val
                if r + 1 < len(nums):
                    prefix[r+1] -= val
            for i in range(1,len(nums)):
                prefix[i] += prefix[i-1]
            for i in range(len(nums)):
                if nums[i] > prefix[i]:
                    return False
            return True
            

        low, high = 0, len(queries)
        while low <= high:
            mid = (high + low) // 2
            if check(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low if low <= len(queries) else -1
                
                
