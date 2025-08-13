class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        ROWS, COLS = len(board), len(board[0])

        # capture unsurrounded regions
        def dfs(row,col):
            if row < 0 or col < 0 or row == ROWS or col == COLS or board[row][col] != "O":
                return
            board[row][col] = "T"
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                dfs(new_row,new_col)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1])):
                    dfs(r,c)

        # capture surrounded regions
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O":
                    board[i][j] = "X"

        # uncapture unsurrounded regions
        for x in range(ROWS):
            for y in range(COLS):
                if board[x][y] == "T":
                    board[x][y] = "O"


        