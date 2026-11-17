class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def inbound(row, col, n, m):
            return 0 <= row < n and 0 <= col < m and grid[row][col] == 0

        boundary_cells = []
        for i in range(m):
            if grid[0][i] == 0:
                boundary_cells.append((0, i))
            if grid[n - 1][i] == 0:
                boundary_cells.append((n - 1, i))
        for i in range(1, n - 1):
            if grid[i][0] == 0:
                boundary_cells.append((i, 0))
            if grid[i][m - 1] == 0:
                boundary_cells.append((i, m - 1))
        
        queue = deque(boundary_cells)
        seen = set(boundary_cells)
        while queue:
            r, c = queue.popleft()
            grid[r][c] = 1
            for ri, ci in directions:
                new_row, new_col = r + ri, c + ci
                if inbound(new_row, new_col, n, m) and (new_row, new_col) not in seen:
                    queue.append((new_row, new_col))
                    seen.add((new_row, new_col))
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    count += 1
                    queue = deque([(i, j)])
                    seen = set((i, j))
                    while queue:
                        r, c = queue.popleft()
                        grid[r][c] = 1
                        for ri, ci in directions:
                            new_row, new_col = r + ri, c + ci
                            if inbound(new_row, new_col, n, m) and (new_row, new_col) not in seen:
                                queue.append((new_row, new_col))
                                seen.add((new_row, new_col))
                    
        return count
        
        