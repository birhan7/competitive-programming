class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        def inbound(row, col, n, m):
            return 0 <= row < n and 0 <= col < m
        n, m = len(maze), len(maze[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque([entrance])
        seen = set(tuple(entrance))
        bredth = 0
        while queue:
            length = len(queue)
            for _ in range(length):
                row, col = queue.popleft()
                for (r, c) in directions:
                    new_row, new_col = row + r, col + c
                    if inbound(new_row, new_col, n, m):
                        if not maze[new_row][new_col] == "+" and (new_row, new_col) not in seen:
                            queue.append((new_row, new_col))
                            seen.add((new_row, new_col))
                    elif [row, col] != entrance:
                        return bredth
            bredth += 1
        return -1
        