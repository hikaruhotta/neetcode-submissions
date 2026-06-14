import math

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) * len(matrix[0]) - 1
        while left <= right:
            mid = left + (right - left) // 2
            row, col = self.indexToRowCol(matrix, mid)

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False



    def indexToRowCol(self, matrix, index):
        num_rows, num_cols = len(matrix), len(matrix[0])

        row = index // num_cols

        col = index % num_cols

        return (row, col)
