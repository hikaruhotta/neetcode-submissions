from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_adj, atlantic_adj = [], []

        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if row == 0 or col == 0:
                    pacific_adj.append((row, col))
                if row == len(heights) - 1 or col == len(heights[0]) - 1:
                    atlantic_adj.append((row, col))

        pacific = self.bfs(heights, pacific_adj)
        atlantic = self.bfs(heights, atlantic_adj)
        print(pacific)
        print(atlantic)

        both = pacific.intersection(atlantic)
        return [[x, y] for (x, y) in both]


    def bfs(self, heights: List[List[int]], seed: List[Tuple]) -> Set:
        queue = deque(seed)
        visited = set(seed)

        while queue:
            r, c = queue.popleft()

            for x, y in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                nr, nc = r + x, c + y
                if self.inbounds(heights, nr, nc) and heights[nr][nc] >= heights[r][c] and (nr, nc) not in visited:
                    queue.append((nr, nc))
                    visited.add((nr, nc))
        
        return set(visited)

    def inbounds(self, heights: List[List[int]], row: int, col: int) -> bool:
        return row >= 0 and row < len(heights) and col >= 0 and col < len(heights[0])