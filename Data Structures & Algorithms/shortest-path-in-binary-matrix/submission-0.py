class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1

        length = 1
        level = [(0, 0)]
        visited = set()

        while level:
            next_level = []
            for (row, col) in level:
                if row == len(grid) - 1 and col == len(grid[0]) - 1:
                    return length

                visited.add((row, col))
                for row_offset in [-1, 0, 1]:
                    for col_offset in [-1, 0, 1]:
                        if row_offset == 0 and col_offset == 0:
                            continue
                        
                        next_row, next_col = row + row_offset, col + col_offset
                        if  (next_row, next_col) not in visited and self.in_bounds(next_row, next_col, grid) and grid[next_row][next_col] == 0:
                            next_level.append((next_row, next_col))
            level = next_level
            length += 1
        
        return -1


    def in_bounds(self, row, col, grid) -> bool:
        return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])

