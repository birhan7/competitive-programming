class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_left, max_right = height[l], height[r]
        ans = 0
        while l < r:
            if height[l] <= height[r]:
                have = max_left - height[l]
                if height[l] > max_left:
                    max_left = height[l]
                ans += have if have > 0 else 0
                l += 1
            else:
                have = max_right - height[r]
                if height[r] > max_right:
                    max_right = height[r]
                ans += have if have > 0 else 0
                r -= 1
        return ans

        

        