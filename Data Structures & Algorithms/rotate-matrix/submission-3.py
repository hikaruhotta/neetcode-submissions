class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # transpose
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # mirror horizontally 
        for row in range(len(matrix)):
            for col in range(len(matrix) // 2):
                matrix[row][col], matrix[row][len(matrix) - col - 1] = matrix[row][len(matrix) - col - 1], matrix[row][col] 


        