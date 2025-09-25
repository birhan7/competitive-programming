class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def backtrack(i,n):
            if i >= n:
                return 0
            if (i, n) not in memo:
                if i == 0:
                    memo[(i, n)] = max(backtrack(i + 1, n), nums[i] + backtrack(i + 2, n - 1))
                else:
                    memo[(i, n)] = max(backtrack(i + 1, n), nums[i] + backtrack(i + 2, n))
            return memo[(i, n)]
        return backtrack(0, n)
        