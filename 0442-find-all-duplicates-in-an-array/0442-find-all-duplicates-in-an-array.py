class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = set()
        for i in range(len(nums)):
            to_index = nums[i] - 1
            while to_index != i:
                if nums[to_index] == nums[i]:
                    ans.add(nums[to_index])
                    break
                else:
                    nums[to_index], nums[i] = nums[i], nums[to_index]
                    to_index = nums[i] - 1
        return  list(ans)

        