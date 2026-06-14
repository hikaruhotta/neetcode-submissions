class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_cycles = 0
        while self.iteration(grid) > 0:
            num_cycles += 1
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return -1
        
        return num_cycles


        
    def iteration(self, grid) -> int:
        new_rotten = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    for i, j in [
                        (-1, 0), (1, 0), (0, -1), (0, 1)
                    ]:
                        next_row, next_col = row + i, col + j
                        if self.inbounds(grid, next_row, next_col) and grid[next_row][next_col] == 1:
                            grid[next_row][next_col] = 3
                            new_rotten += 1
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 3:
                    grid[row][col] = 2
        
        return new_rotten


    def inbounds(self, grid, row, col):
        return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])