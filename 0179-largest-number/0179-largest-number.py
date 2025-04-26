class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        nums.sort(reverse=True)
        for i in range(len(nums)):
            j = i - 1
            while j >= 0 and nums[j] + nums[j+1] < nums[j+1] + nums[j]:
                nums[j] , nums[j+1] = nums[j+1] , nums[j]
                j -= 1
        string = "".join(nums)
        return str(int(string))


        