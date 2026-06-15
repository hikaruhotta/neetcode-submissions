from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    self.helper(grid, row, col)
                    result += 1
        
        return result
    
    def helper(self, grid: List[List[str]], row: int, col: int) -> None:
        queue = deque([(row, col)])

        while queue:
            (row, col) = queue.popleft()
            for x, y in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                next_row, next_col = row + x, col + y
                if self.inbounds(grid, next_row, next_col) and grid[next_row][next_col] == '1':
                    queue.append((next_row, next_col))
            grid[row][col] = '2'
    

    def inbounds(self, grid: List[List[int]], row: int, col: int) -> bool:
        return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])
