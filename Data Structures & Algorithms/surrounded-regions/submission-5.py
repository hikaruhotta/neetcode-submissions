from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'O':
                    self.dfs(board, row, col)
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'Y':
                    board[row][col] = 'O'
                    

    def dfs(self, board, row, col):
        visited = set()
        queue = deque([(row, col)])

        on_border = False

        while queue:
            row, col = queue.popleft()
            if not self.not_border(board, row, col):
                on_border = True

            visited.add((row, col))

            for i, j in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                next_row, next_col = row + i, col + j
                if self.in_bounds(board, next_row, next_col) and board[next_row][next_col] == 'O' and (next_row, next_col) not in visited:
                    queue.append((next_row, next_col))

        if not on_border:
            for row, col in visited:
                board[row][col] = 'X'
        else:
            for row, col in visited:
                board[row][col] = 'Y'


    def in_bounds(self, board, row, col):
        return row >= 0 and row < len(board) and col >= 0 and col < len(board[0])
    
    def not_border(self, board, row, col):
        return row != 0 and row != len(board) - 1 and col != 0 and col != len(board[0]) - 1


# [
#     ["X","X","X","X","O","X"]
#     ["O","X","X","O","O","X"]
#     ["X","O","X","O","O","O"]
#     ["X","O","O","O","X","O"]
#     ["O","O","X","X","O","X"]
#     ["X","O","X","O","X","X"]
# ]

# [
#     ["X","X","X","X","O","X"]
#     ["O","X","X","X","O","X"]
#     ["X","O","X","X","O","O"]
#     ["X","O","O","X","X","O"]
#     ["O","O","X","X","X","X"]
#     ["X","O","X","O","X","X"]
# ]


