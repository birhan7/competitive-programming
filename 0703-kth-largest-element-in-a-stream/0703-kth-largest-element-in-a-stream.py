class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        heapify(self.heap)
        self.k = k
        while k < len(self.heap):
            heappop(self.heap)
        
    def add(self, val: int) -> int:
        heappush(self.heap,val)
        length = len(self.heap)
        if length > self.k:
            heappop(self.heap)
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)