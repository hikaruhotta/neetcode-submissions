import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        min_heap = []
        heapq.heappush(min_heap, (grid[0][0], (0, 0))) 
        visited = set()

        while min_heap:
            max_path_elevation, (row, col) = heapq.heappop(min_heap)
            
            if (row, col) in visited:
                continue

            visited.add((row, col))
            
            if (row, col) == (len(grid) - 1, len(grid[0]) - 1):
                return max_path_elevation
            
            for x, y in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                nr, nc = row + x, col + y
                if self.inbounds(grid, nr, nc) and (nr, nc) not in visited:
                    heapq.heappush(min_heap, (max(grid[nr][nc], max_path_elevation), (nr, nc)))
        
        return -1

    
    def inbounds(self, grid: List[List[int]], row: int, col: int) -> bool:
        return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])