class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        for col in range(size//2):
            print("sss")
            for row in range(col , size - 1 - col):
                # store bottom-left
                temp = matrix[size-1-row][col]

                # bottom-right to bottom-left
                matrix[size-1-row][col] = matrix[size-1-col][size-1-row]

                # top-right to bottom-right
                matrix[size-1-col][size-1-row] = matrix[row][size-1-col]

                #top-left to top-right
                matrix[row][size-1-col] = matrix[col][row]
                
                # stored bottom-left to top-left
                matrix[col][row] = temp
        return matrix




        