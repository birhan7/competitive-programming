class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        l, r = 0, 0
        n, m = len(firstList), len(secondList)
        ans = []
        while l < n and r < m:
            l1, r1 = firstList[l]
            l2, r2 = secondList[r]
            start = max(l1, l2)
            end = min(r1, r2)
            if start <= end:
                ans.append([start, end])
            if r1 < r2:
                l += 1
            else:
                r += 1

        return ans
