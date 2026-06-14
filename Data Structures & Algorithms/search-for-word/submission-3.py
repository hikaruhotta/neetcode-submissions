class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0] and self.helper(board, word[1:], row, col, set([(row, col)])):
                    return True
        return False
    
    def helper(self, board: List[List[str]], word: str, row: int, col: int, visited: Set) -> bool:
        if len(word) == 0:
            return True

        results = []
        for x, y in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            next_row, next_col = row + x, col + y
            if self.in_bounds(board, next_row, next_col) and board[next_row][next_col] == word[0] and (next_row, next_col) not in visited:
                visited.add((next_row, next_col))
                results.append(self.helper(board, word[1:], next_row, next_col, visited))
                visited.remove((next_row, next_col))
        return any(results)
    
    
    def in_bounds(self, board: Lits[List[int]], row: int, col: int) -> bool:
        return row >= 0 and row < len(board) and col >= 0 and col < len(board[0])