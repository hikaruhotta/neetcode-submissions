import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        min_heap = []
        heapq.heappush(min_heap, (0, (0, 0)))
        visited = set()

        while min_heap:
            effort, (row, col) = heapq.heappop(min_heap)
            if (row, col) in visited:
                continue
            
            visited.add((row, col))
            if row == len(heights) - 1 and col == len(heights[0]) - 1:
                return effort

            for x, y in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                nr, nc = row + x, col + y
                if self.inbounds(heights, nr, nc) and (nr, nc) not in visited:
                    e = max(effort, abs(heights[nr][nc] - heights[row][col]))
                    heapq.heappush(min_heap, (e, (nr, nc)))
        
        return -1
    
    def inbounds(self, heights: List[[List[int]]], row: int, col: int) -> bool:
        return row >= 0 and row < len(heights) and col >= 0 and col < len(heights[0])
            


