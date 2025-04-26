class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        index = 0
        while index < len(nums)-1:
            if nums[index] == nums[index+1]:
                nums[index] = nums[index] * 2
                nums[index+1] = 0
                index += 2
            else:
                index += 1
        if 0 in nums:
            left = nums.index(0)
            right = left + 1
            while right < len(nums):
                if nums[left] == 0 and nums[right] != 0:
                    nums[left],nums[right] = nums[right],nums[left]
                elif nums[left] == 0 and nums[right] == 0:
                    right += 1
                else:
                    left += 1
                    right += 1

        return nums
        