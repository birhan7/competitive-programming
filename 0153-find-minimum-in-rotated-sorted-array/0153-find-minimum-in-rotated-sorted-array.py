class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        min_val = nums[0]
        while low <= high:
            mid = (low + high)//2
            min_val = min(min_val,nums[mid])
            if nums[low] > nums[high]:
                if nums[mid] >= nums[low]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                min_val = min(min_val,nums[low])
                break
        return min_val
        

        