class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def divide(l, r):
            if r - l == 0:
                return l
            ans = -1
            if r - l == 2:
                if nums[l] < nums[l + 1] and nums[l + 1] > nums[r]:
                    return l + 1
            elif r - l == 1:
                if nums[l] > nums[r]:
                    return l
            elif r - l > 2:
                mid = (l + r) // 2
                ans = max(ans ,divide(l, mid))
                ans = max(ans, divide(mid - 1, mid + 1))
                ans = max(ans, divide(mid, r))
            return ans
        return divide(0, len(nums) - 1)
        