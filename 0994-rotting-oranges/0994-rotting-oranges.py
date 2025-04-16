class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def inbound(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        fresh, time = 0, 0
        n, m = len(grid), len(grid[0])
        queue = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append([i,j])
                elif grid[i][j] == 1:
                    fresh += 1
        while queue and fresh > 0:
            length = len(queue)
            for _ in range(length):
                row, col = queue.popleft()
                for dx, dy in directions:
                    new_row, new_col = dx + row, dy + col
                    if inbound(new_row, new_col) and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        fresh -= 1
                        queue.append([new_row,new_col])
            time += 1
        return time if fresh == 0 else -1
        
        