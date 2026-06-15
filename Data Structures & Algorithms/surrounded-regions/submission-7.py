from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        self.visited = set()
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O" and (row, col) not in self.visited:
                    self.helper(board, row, col)
    
    def helper(self, board: [List[List[str]]], row: int, col: int) -> None:
        region = []
        self.visited.add((row, col))

        queue = deque([(row, col)])

        while queue:
            row, col = queue.popleft()
            region.append((row, col))

            for x, y in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                nr, nc = row + x, col + y
                if self.inbounds(board, nr, nc) and board[nr][nc] == 'O' and (nr, nc) not in self.visited:
                    queue.append((nr, nc))
                    self.visited.add((nr, nc))

        is_surrounded = True
        for row, col in region:
            if row == 0 or row == len(board) - 1 or col == 0 or col == len(board[0]) - 1:
                is_surrounded = False
                break

        if is_surrounded:
            for row, col in region:
                board[row][col] = 'X'



    def inbounds(self, board: [List[List[str]]], row: int, col: int) -> bool:
        return row >= 0 and row < len(board) and col >= 0 and col < len(board[0])


