class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # mirror horizontally 
        for row in range(len(matrix) // 2):
            for col in range(len(matrix)):
                matrix[row][col], matrix[len(matrix) - row - 1][col] = matrix[len(matrix) - row - 1][col], matrix[row][col]

        # mirror on \
        for row in range(len(matrix)):
            for col in range(row, len(matrix)):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        