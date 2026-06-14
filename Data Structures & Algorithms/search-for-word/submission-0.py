class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(word) == 0:
            return False

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    tmp = board[row][col]
                    board[row][col] = '#'
                    if self.existHelper(board, word[1:], row, col):
                        return True
                    board[row][col] = tmp
        
        return False

    def existHelper(self, board, word, row, col):
        if len(word) == 0:
            return True

        for i, j in [
            (-1, 0), (1, 0), (0, -1), (0, 1)
        ]:
            next_row, next_col = row + i, col + j
            if self.inbounds(board, next_row, next_col) and board[next_row][next_col] == word[0] and board[next_row][next_col] != '#':
                tmp = board[next_row][next_col]
                board[next_row][next_col] = '#'
                if self.existHelper(board, word[1:], next_row, next_col):
                    return True
                board[next_row][next_col] = tmp

        return False

    def inbounds(self, board, row, col) -> bool:
        return row >= 0 and row < len(board) and col >= 0 and col < len(board[0])