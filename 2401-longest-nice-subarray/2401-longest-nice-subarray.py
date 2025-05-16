class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l, n = 0, len(nums)
        OR = nums[0]
        count = 1
        for r in range(1,n):
            if OR & nums[r] == 0:
                count = max(count, r - l + 1)
            else:
                while l < r and (OR & nums[r] != 0):
                    OR ^= nums[l]
                    l += 1
            OR |= nums[r]
        return count
            



        