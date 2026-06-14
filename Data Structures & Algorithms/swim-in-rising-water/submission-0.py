import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        min_heap = [(grid[0][0], (0, 0))]

        res_times = {}

        while min_heap:
            max_elevation, (row, col) = heapq.heappop(min_heap)

            if (row, col) in res_times:
                continue
            
            res_times[(row, col)] = max_elevation

            for i, j in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                next_row, next_col = row + i, col + j
                if self.isInBounds(grid, next_row, next_col):
                    heapq.heappush(min_heap, (max(max_elevation, grid[next_row][next_col]), (next_row, next_col)))
        
        return res_times[(len(grid) - 1, len(grid[0]) - 1)]


    def isInBounds(self, grid, row, col):
        return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])


