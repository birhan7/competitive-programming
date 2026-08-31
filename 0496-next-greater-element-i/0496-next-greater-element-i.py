class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        deque = collections.deque([-1])
        next_greater = {}
        for i in range(len(nums2) - 1, -1, -1):
            value = nums2[i]
            for j in range(len(deque)):
                if deque[j] > value:
                    next_greater[value] = deque[j]
                    break
            else:
                next_greater[value] = -1
            deque.appendleft(value)
        ans = []
        for i in range(len(nums1)):
            ans.append(next_greater[nums1[i]])
        return ans
