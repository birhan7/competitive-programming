class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        n = len(grid)
        res = 0
        heap = []
        heapify(heap)
        
        for i in range(n):
            for j in range(len(grid[i])):
                grid[i][j] = -1 * grid[i][j]
            heapify(grid[i])

        for i in range(n):
            m = limits[i]
            for _ in range(m):
                if grid[i]:
                    heappush(heap,heappop(grid[i]))
                else:
                    break
        
        while k != 0:
            res += abs(heappop(heap))
            k -= 1
        return res


            

        