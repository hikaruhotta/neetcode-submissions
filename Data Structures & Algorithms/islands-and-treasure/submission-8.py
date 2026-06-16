import heapq

class Solution:
    
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        min_heap = []
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    heapq.heappush(min_heap, (0, row, col))
                    visited.add((row, col))
        
        while min_heap:
            distance, row, col = heapq.heappop(min_heap)
            if grid[row][col] not in (-1, 0):
                grid[row][col] = min(grid[row][col], distance)
            
            for x, y in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                nr, nc = row + x, col + y
                if self.inbounds(grid, nr, nc) and grid[nr][nc] not in (-1, 0) and (nr, nc) not in visited:
                    heapq.heappush(min_heap, (distance + 1, nr, nc))
                    visited.add((nr, nc))

    def inbounds(self, grid: List[List[int]], row: int, col: int) -> bool:
        return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])
             