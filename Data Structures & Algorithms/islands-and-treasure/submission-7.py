import heapq

INF = 2147483647

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
            path_len, r, c  = heapq.heappop(min_heap)
            if grid[r][c] not in (-1, 0):
                grid[r][c] = min(grid[r][c], path_len)
            
            for x, y in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                nr, nc = r + x, c + y
                if self.inbounds(grid, nr, nc) and (nr, nc) not in visited and grid[nr][nc] != -1:
                    print("yo")
                    visited.add((nr, nc))
                    heapq.heappush(min_heap, (path_len + 1, nr, nc))
                    

    def inbounds(self, grid: List[List[int]], row: int, col: int) -> bool:
        return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])
