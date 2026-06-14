class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix_sum =  [[0 for col in range(len(matrix[0]))] for row in range(len(matrix))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                total = 0

                if row > 0:
                    total += self.matrix_sum[row - 1][col]
                if col >= 0:
                    total += self.matrix_sum[row][col - 1]
                if row > 0 and col > 0:
                    total -= self.matrix_sum[row - 1][col - 1]

                total += matrix[row][col]

                self.matrix_sum[row][col] = total
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # 2, 1, 4, 3

        total = 0

        total += self.matrix_sum[row2][col2]

        if row1 > 0:
            total -= self.matrix_sum[row1 - 1][col2]
        
        if col1 > 0:
            total -= self.matrix_sum[row2][col1 - 1]
        
        if row1 > 0 and col1 > 0:
            total += self.matrix_sum[row1 - 1][col1 - 1]
        
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)