class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        self.obstacleGrid = obstacleGrid
        self.cache = [[-float('inf') for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        result = self.dfs(0, 0)
        if result == -float('inf'):
            return 0
        return result

    def dfs(self, row, col) -> int:
        if self.obstacleGrid[row][col] == 1:
            return 0

        if row == len(self.obstacleGrid) -1 and col == len(self.obstacleGrid[0]) - 1:
            return 1

        if self.cache[row][col] != -float('inf'):
            return self.cache[row][col]
        
        result = 0
        for i, j in [(1, 0), (0, 1)]:
            next_row, next_col = row + i, col + j
            if self.isInBounds(next_row, next_col):
                result += self.dfs(next_row, next_col)

        self.cache[row][col] = result
        return result
        
    def isInBounds(self, row, col):
        return row >= 0 and row < len(self.obstacleGrid) and col >= 0 and col < len(self.obstacleGrid[0])