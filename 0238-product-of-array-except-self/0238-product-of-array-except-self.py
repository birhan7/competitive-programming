class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, suffix = [], [1] * n
        mult = 1
        for i in range(n):
            mult *= nums[i]
            prefix.append(mult)

        mult = 1
        for i in range(n - 1, -1, -1):
            mult *= nums[i]
            suffix[i] = mult
        
        ans = []
        for i in range(n):
            temp = 1
            if i - 1 >= 0:
                temp *= prefix[i - 1]
            if i + 1 < n:
                temp *= suffix[i + 1]
            ans.append(temp)
        return ans
        