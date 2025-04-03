class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            to_index = nums[i] - 1
            while to_index != i:
                if nums[to_index] != nums[i]:
                    if to_index in dic:
                        del dic[to_index]
                    nums[i], nums[to_index] = nums[to_index], nums[i]
                    to_index = nums[i] - 1
                else:
                    dic[i] = i + 1
                    break
        return list(dic.values())