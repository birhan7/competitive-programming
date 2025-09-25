class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def robthem(i):
            if i >= n:
                return 0
            if i not in memo:
                include = robthem(i + 2) + nums[i]
                exclude = robthem(i + 1)
                memo[i] = max(include, exclude)
            return memo[i]
        return robthem(0)
        