class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = []
        for i in range(1,n+1):
            nums.append(i)
        index = 0
        while len(nums) > 1:
            index = ((index - 1)+ k) % len(nums)
            nums.remove(nums[index])
        return nums[0]


        