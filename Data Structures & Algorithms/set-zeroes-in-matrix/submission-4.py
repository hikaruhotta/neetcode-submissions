class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # for row = 0 or col = 0:
        # if 0 and entire row/col should be 0, process row/col and set to -1
        # if 1 and entire row/col should be 0, process row/col and set to -2

        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                # ALREADY PROCESSED
                if matrix[row][col] != 0:
                    continue

                if matrix[row][0] not in (-1, -2):
                    matrix[row][0] = -1 if matrix[row][0] == 0 else -2
                
                if matrix[0][col] not in (-1, -2):
                    matrix[0][col] = -1 if matrix[0][col] == 0 else -2

        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[row][0] in (0, -1, -2) or matrix[0][col] in (0, -1, -2):
                    matrix[row][col] = 0 
        
        row_any_zero = any([matrix[row][0] in (0, -1) for row in range(len(matrix))])
        if row_any_zero:
            for row in range(1, len(matrix)):
                matrix[row][0] = 0
        
        col_any_zero = any([matrix[0][col] in (0, -1) for col in range(len(matrix[0]))])
        if col_any_zero:
            for col in range(1, len(matrix[0])):
                matrix[0][col] = 0

        if row_any_zero or col_any_zero:
            matrix[0][0] = 0

        for row in range(1, len(matrix)):
                if matrix[row][0] in (-1, -2):
                    matrix[row][0] = 0
        
        for col in range(1, len(matrix[0])):
                if matrix[0][col] in (-1, -2):
                    matrix[0][col] = 0


        


                



        