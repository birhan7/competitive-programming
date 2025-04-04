class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        missing, duplicate = 0, 0
        ans = set()
        for i in range(len(nums)):
            to_index = nums[i] - 1
            while to_index != i:
                if nums[to_index] == nums[i]:
                    missing = i + 1
                    duplicate = nums[i]
                    break
                else:
                    if nums[i] == missing:
                        missing = 0
                    nums[to_index], nums[i] = nums[i], nums[to_index]
                    to_index = nums[i] - 1
        return [duplicate,missing]
        