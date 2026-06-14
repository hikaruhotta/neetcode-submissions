class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.num_islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    self.num_islands += 1
                    self.helper(row, col, grid)
        return self.num_islands

    def helper(self, row, col, grid):
        queue = [(row, col)]
        while queue:
            curr_row, curr_col = queue.pop()
            grid[curr_row][curr_col] = "2"

            for row_offset, col_offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                next_row, next_col = curr_row + row_offset, curr_col + col_offset
                if self.is_inbounds(next_row, next_col, grid) and grid[next_row][next_col] == "1":
                    queue.append((next_row, next_col))

    def is_inbounds(self, row, col, grid):
        return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])