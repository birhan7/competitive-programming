class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        length = len(nums)
        summ = sum(nums)
        if summ % 2 != 0:
            return False
        target_sum = summ // 2
        memo = {}
        def backtrack(index, current):
            if index >= length:
                return False
            if current == target_sum:
                return True
            if (index, current) not in memo:
                if current + nums[index] <= target_sum:
                    if backtrack(index + 1, current + nums[index]):
                        memo[(index, current)] = True
                        return memo[(index, current)]
                exclude = backtrack(index + 1, current)
                memo[(index, current)] = exclude
            return memo[(index, current)]
        return backtrack(0, 0)
        