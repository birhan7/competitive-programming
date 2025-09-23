class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def backtrack(index):
            if index >= n:
                return 0
            if index not in memo:
                memo[index] = 1
                for j in range(index + 1, n):
                    if nums[j] > nums[index]:
                        memo[index] = max(1 + backtrack(j), memo[index])
            return memo[index]
        ans = 1
        for i in range(n):
            ans = max(ans, backtrack(i))
        return ans
        