class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        sys.setrecursionlimit(20000)
        self.cache = {}
        self.matrix = matrix
        
        max_result = 0
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[0])):
                max_result = max(max_result, self.helper(row, col))
    
        return max_result
    
    def helper(self, row: int, col: int) -> int:
        if (row, col) in self.cache:
            return self.cache[(row, col)]

        result = 1
        for x, y in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            nr, nc = row + x, col + y
            if self.inbounds(nr, nc) and self.matrix[nr][nc] > self.matrix[row][col]:
                result = max(result, 1 + self.helper(nr, nc))
        
        self.cache[(row, col)] = result
        return result

    
    def inbounds(self, row: int, col: int) -> bool:
        return row >= 0 and row < len(self.matrix) and col >= 0 and col < len(self.matrix[0])