import math

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows, num_cols = len(matrix), len(matrix[0])
        n = num_rows * num_cols
        left, right = 0, n - 1

        while left <= right:
            mid = left + (right - left) // 2
            row, col = self.indexToMatrixIndices(mid, num_rows, num_cols)
            print(row, col)
            val = matrix[row][col]
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False

    def indexToMatrixIndices(self, i: int, num_rows, num_cols):
        row = i // num_cols
        col = i % num_cols
        return (row, col)
