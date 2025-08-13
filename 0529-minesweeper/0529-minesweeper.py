class Solution:
    def getNumMines(self,board,x,y):
        count = 0
        for r in range(x-1,x+2):
            for c in range(y-1,y+2):
                if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == "M":
                    count += 1
        return count

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
            r, c = click
            if board[r][c] == "M":
                board[r][c] = "X"

            elif board[r][c] == "E":
                numMines = self.getNumMines(board,r,c)
                if numMines:
                    board[r][c] = str(numMines)
                else:
                    board[r][c] = "B"
                    for row in range(r-1,r+2):
                        for col in range(c-1,c+2):
                            if 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] != "B":
                                self.updateBoard(board,[row,col])
            
            return board
