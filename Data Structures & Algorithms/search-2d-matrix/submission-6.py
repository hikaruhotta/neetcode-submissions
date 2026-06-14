class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L, R = 0, len(matrix) * len(matrix[0]) - 1

        while L <= R:
            M = L + (R - L) // 2
            M_val = self.getValue(matrix, M)

            if M_val == target:
                return True
            elif M_val > target:
                R = M - 1
            else:
                L = M + 1
        
        return False
            

    def getValue(self, matrix: List[List[int]], index: int) -> int:
        num_cols = len(matrix[0])
        col_index = index % num_cols
        row_index = index // num_cols
        return matrix[row_index][col_index]

