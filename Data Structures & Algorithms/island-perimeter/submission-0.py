from collections import deque

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return self.helper(grid, row, col)
        return 0
    
    def helper(self, grid: List[List[int]], row: int, col: int) -> int:
        result = 0
        queue = deque([(row, col)])
        visited = set([(row, col)])

        while queue:
            r, c = queue.popleft()
            for x, y in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                nr, nc = r + x, c + y
                if not self.inbounds(grid, nr, nc) or grid[nr][nc] == 0:
                    result += 1
                elif (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc))
        
        return result

        
    def inbounds(self, grid: List[List[int]], row: int, col: int) -> bool:
        return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])