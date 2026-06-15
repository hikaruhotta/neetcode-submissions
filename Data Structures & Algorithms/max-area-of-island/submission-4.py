from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    result = max(result, self.bfs(grid, row, col))
        return result
    
    def bfs(self, grid: List[List[int]], row: int, col: int) -> int:
        result = 0
        queue = deque([(row, col)])
        grid[row][col] = 2

        while queue:
            (row, col) = queue.popleft()
            for x, y in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                next_row, next_col = row + x, col + y
                if self.inbounds(grid, next_row, next_col) and grid[next_row][next_col] == 1:
                    queue.append((next_row, next_col))
                    grid[next_row][next_col] = 2
            result += 1
        return result
        

    def inbounds(self, grid: List[List[int]], row: int, col: int) -> bool:
        return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])