class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        n, m = len(mat), len(mat[0])
        row, col = 0, 0
        up = True
        while row < n and col < m:
            if up:
                while row > 0 and col < m - 1:
                    ans.append(mat[row][col])
                    row, col = row - 1, col + 1
                ans.append(mat[row][col])
                if col == m - 1:
                    row += 1
                else:
                    col += 1
            else:
                while col > 0 and row < n - 1:
                    ans.append(mat[row][col])
                    row, col = row + 1, col - 1
                ans.append(mat[row][col])
                if row == n - 1:
                    col += 1
                else:
                    row += 1
            up = not up
        return ans

                


        