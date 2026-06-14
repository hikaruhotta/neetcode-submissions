class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_index = 0

        row, col = 0, 0

        while True:
            result.append(matrix[row][col])
            matrix[row][col] = 999

            prev_row, prev_col = row, col

            for offset in range(len(dirs)):
                dir_index = (dir_index + offset) % len(dirs)
                next_row, next_col = row + dirs[dir_index][0], col + dirs[dir_index][1]
                # can continue in same direction
                if self.inBounds(next_row, next_col, matrix) and matrix[next_row][next_col] != 999:
                    row, col = next_row, next_col
                    break
            
            # at center
            if row == prev_row and col == prev_col:
                break
        
        return result

        
    def inBounds(self, row, col, matrix) -> bool:
        return row >= 0 and row < len(matrix) and col >= 0 and col < len(matrix[0])

