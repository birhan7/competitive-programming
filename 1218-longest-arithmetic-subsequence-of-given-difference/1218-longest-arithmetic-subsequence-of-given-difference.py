class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        length = 0
        memo = {}
        for i in arr:
            if i - difference in memo:
                memo[i] = memo[i - difference] + 1
            else:
                memo[i] = 1
            length = max(length, memo[i])
        return length

            
        