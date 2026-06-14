class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)

        matrix.reverse()

        # mirror x = y
        for row in range(N):
            for col in range(row + 1, N):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]



