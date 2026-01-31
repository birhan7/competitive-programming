class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.prefix = [[0] * (cols) for _ in range(rows + 1)]

        for r in range(rows):
            total = 0
            for c in range(cols):
                total += matrix[r][c]
                self.prefix[r + 1][c] += self.prefix[r][c] + total

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, r2 = row1 + 1, row2 + 1
        total = self.prefix[r2][col2]
        top = self.prefix[r1 - 1][col2]
        left = self.prefix[r2][col1 - 1] if col1 - 1 >= 0 else 0
        include = self.prefix[r1 - 1][col1 - 1] if col1 - 1 >= 0 else 0

        return total - top - left + include
        


        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)