class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapify(stones)
        print(stones)
        while len(stones) >= 2:
            stone1, stone2 = heappop(stones), heappop(stones)
            if stone1 < stone2:
                heappush(stones,stone1-stone2)
                print(stones)
        return abs(stones[0]) 
        