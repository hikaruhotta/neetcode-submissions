from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.max_island_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    area = self.helper(grid, row, col)
                    self.max_island_area = max(self.max_island_area, area)

        return self.max_island_area
    
    def helper(self, grid: List[List[int]], row: int, col: int) -> int:
        queue = deque([(row, col)])
        grid[row][col] = -1
        area = 0
        while queue:
            i, j = queue.popleft()
            area += 1
            for row_offset, col_offset in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                next_row, next_col = i + row_offset, j + col_offset
                if self.is_inbounds(grid, next_row, next_col) and grid[next_row][next_col] == 1:
                    queue.append((next_row, next_col))
                    grid[next_row][next_col] = -1
                    
        return area

    def is_inbounds(self, grid: List[List[int]], row: int, col: int):
        return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])


