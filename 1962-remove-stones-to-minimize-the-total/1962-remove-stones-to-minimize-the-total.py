class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        heapify(heap)

        for pile in piles:
            heappush(heap,-1 * pile)
        
        for _ in range(k):
            val = heappop(heap)
            heappush(heap,math.floor(val/2))
        return -1 * sum(heap)
