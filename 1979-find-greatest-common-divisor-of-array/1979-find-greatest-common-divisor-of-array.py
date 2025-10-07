class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        small, large = nums[0], nums[-1]
        return math.gcd(large,small)
        