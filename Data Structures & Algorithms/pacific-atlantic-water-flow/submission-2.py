from collections import deque 

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:        
        pacific = self.pacific(heights)
        atlantic = self.atlantic(heights)

        return [[row, col] for row, col in pacific & atlantic]

    def pacific(self, heights):
        visited = set()
        queue = deque([])

        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if row == 0 or col == 0:
                    queue.append((row, col))
        
        while queue:
            row, col = queue.popleft()
            visited.add((row, col))
            
            for i, j in [
                (0, -1), (0, 1), (-1, 0), (1, 0)
            ]:
                next_row, next_col = row + i, col + j
                if self.inbounds(heights, next_row, next_col) and (next_row, next_col) not in visited and heights[next_row][next_col] >= heights[row][col]:
                    queue.append((next_row, next_col))

        return visited

    def atlantic(self, heights):
        visited = set()
        queue = deque([])

        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if row == len(heights) - 1 or col == len(heights[0]) - 1:
                    queue.append((row, col))
        
        while queue:
            row, col = queue.popleft()
            visited.add((row, col))
            
            for i, j in [
                (0, -1), (0, 1), (-1, 0), (1, 0)
            ]:
                next_row, next_col = row + i, col + j
                if self.inbounds(heights, next_row, next_col) and (next_row, next_col) not in visited and heights[next_row][next_col] >= heights[row][col]:
                    queue.append((next_row, next_col))

        return visited

    
    def inbounds(self, grid, row, col):
        return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])