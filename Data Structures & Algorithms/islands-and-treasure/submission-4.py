from collections import deque

INF = 2147483647

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque([])
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    queue.append((row, col))
        
        while queue:
            row, col = queue.popleft()
            for i, j in [
                (-1, 0), (1, 0), (0, -1), (0, 1)
            ]:
                next_row, next_col = row + i, col + j
                if self.inbounds(grid, next_row, next_col) and grid[next_row][next_col] == INF:
                    grid[next_row][next_col] = grid[row][col] + 1
                    queue.append((next_row, next_col))

    def inbounds(self, grid, row, col) -> bool:
        return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])
        


