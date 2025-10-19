class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        ans = []
        while left < right and top < bottom:

            # include top row
            for i in range(left, right):
                ans.append(matrix[top][i])
            top += 1

            # include right column
            for i in range(top, bottom):
                ans.append(matrix[i][right - 1])
            right -= 1

            if not(left < right and top < bottom):
                break
            
            # include bottom row
            for i in range(right - 1, left - 1, -1):
                ans.append(matrix[bottom - 1][i])
            bottom -= 1

            # include left column
            for i in range(bottom - 1, top - 1, -1):
                ans.append(matrix[i][left])
            left += 1
        return ans


        