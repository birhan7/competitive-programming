class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        val = 0
        n = len(nums) + 1
        for i in range(n):
            val = val ^ i
        
        for i in range(n - 1):
            val = val ^ nums[i]
        return val


        