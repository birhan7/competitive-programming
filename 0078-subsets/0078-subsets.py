class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        val = 0
        max_val = 1 << n
        res = []
        while val < max_val:
            k = 0
            ans = []
            while k < n:
                temp = val & (1 << k)
                if temp != 0:
                    ans.append(nums[k])
                k += 1
            res.append(ans)
            val += 1
        return res

            

        