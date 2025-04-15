class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        queue = deque()
        def inbound(i,j):
            return 0 <= i < len(isWater) and 0 <= j < len(isWater[0])
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if isWater[i][j] == 1:
                    queue.append((i,j))
                    isWater[i][j] = 0
                else:
                    isWater[i][j] = -1
        while queue:
            i, j = queue.popleft()
            for dx, dy in directions:
                new_row, new_col = dx + i, dy + j
                if inbound(new_row,new_col) and isWater[new_row][new_col] == -1:
                    isWater[new_row][new_col] = isWater[i][j] + 1
                    queue.append((new_row,new_col))
        return isWater

            

        