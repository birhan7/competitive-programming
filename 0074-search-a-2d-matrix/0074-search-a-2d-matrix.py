class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row,col = len(matrix)-1,len(matrix[0])-1

        def check(mid):
            low, high = 0, col
            while low <= high:
                center = (low + high) // 2
                if target == matrix[mid][center]:
                    return True
                elif target > matrix[mid][center]:
                    low = center + 1
                else: 
                    high = center - 1
            return False
                
        low, high = 0, row
        while low <= high:
            mid = (low + high)//2
            if matrix[mid][col] < target:
                low = mid + 1
            elif matrix[mid][0] > target:
                high = mid - 1
            else:
                return check(mid)
        return False