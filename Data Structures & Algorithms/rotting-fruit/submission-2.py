from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        while self.hasFresh(grid):
            new_rotten = self.cycle(grid)
            if new_rotten == 0:
                return -1
            minutes += 1
        return minutes
        
    def hasFresh(self, grid: List[List[int]]) -> bool:
        num_fresh = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    num_fresh += 1
        return num_fresh > 0

    def cycle(self, grid: List[List[int]]) -> None:
        new_rotten = 0
        queue = deque()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row, col))
        
        while queue:
            r, c = queue.popleft()
            for x, y in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                nr, nc = r + x, c + y
                if self.inbounds(grid, nr, nc) and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    new_rotten += 1
        
        return new_rotten
    
    def inbounds(self, grid: List[List[int]], row: int, col: int) -> bool:
        return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])




