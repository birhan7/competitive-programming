class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        length = len(nums)
        memo = {}
        def dfs(i, path):
            if i == length:
                return 1 if path == target else 0
            if (i, path) not in memo:
                count = dfs(i + 1, path + nums[i]) + dfs(i + 1, path - nums[i])
                memo[(i, path)] = count
            return memo[(i, path)]
        return dfs(0, 0)

        