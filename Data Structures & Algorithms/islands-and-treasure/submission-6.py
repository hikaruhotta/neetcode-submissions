from collections import deque

INF = 2147483647

class Solution:

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == INF:
                    self.helper(grid, row, col)
    
    def helper(self, grid: List[List[int]], row: int, col: int) -> None:
        result = INF
        visited = set()

        queue = deque([(row, col, 0)])
        visited.add((row, col))

        while queue:
            r, c, path_len = queue.popleft()
            if grid[r][c] == 0:
                result = min(result, path_len)
            elif grid[r][c] not in (-1, INF):
                result = min(result, path_len + grid[r][c])
            else:
                for x, y in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                    nr, nc = r + x, c + y
                    if self.inbounds(grid, nr, nc) and grid[nr][nc] != -1 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc, path_len + 1)) 
        grid[row][col] = result
        

    def inbounds(self, grid: List[List[int]], row: int, col: int) -> bool:
        return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])
