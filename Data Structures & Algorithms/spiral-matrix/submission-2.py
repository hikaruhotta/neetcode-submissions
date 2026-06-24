class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # right, down, left, up

        dir_i = 0
        row, col = 0, 0
        result.append(matrix[row][col])
        matrix[row][col] = float('inf')

        zero_movement_count = 0

        while True:
            x, y = dirs[dir_i % len(dirs)]
            side_length = 0
            while self.inbounds(matrix, row + x, col + y) and matrix[row + x][col + y] != float('inf'):
                row += x
                col += y
                side_length += 1
                result.append(matrix[row][col])
                matrix[row][col] = float('inf')
            if side_length == 0:
                zero_movement_count += 1
            if zero_movement_count == len(dirs):
                break
            dir_i += 1
        
        return result


    
    def inbounds(self, matrix: List[List[int]], row: int, col: int) -> bool:
        return row >= 0 and row < len(matrix) and col >= 0 and col < len(matrix[0])
