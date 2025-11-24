class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        holder, seeker = 0, 0
        n = len(nums)
        while seeker < n:
            if nums[seeker] != 0:
                nums[seeker], nums[holder] = nums[holder], nums[seeker]
                holder += 1
            seeker += 1
        


        