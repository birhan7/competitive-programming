class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            for length in range(len(nums)):
                if i + length < len(nums):
                    if math.gcd(*nums[i:i + length + 1]) == k:
                        ans += 1
        return ans