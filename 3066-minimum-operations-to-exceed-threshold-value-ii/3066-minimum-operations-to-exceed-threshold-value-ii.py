class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heap = nums
        heapify(heap)
        count = 0
        while len(heap) >= 2:
            min_val, max_val = heappop(heap), heappop(heap)
            if min_val < k or max_val < k:
                heappush(heap,(min_val * 2) + max_val)
                count += 1
            else:
                return count
        return count
        