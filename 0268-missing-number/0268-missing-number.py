class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = set(nums)
        s = set()
        for i in range(len(nums)+1):
            s.add(i)
        return list(s-ans)[0]
        

        