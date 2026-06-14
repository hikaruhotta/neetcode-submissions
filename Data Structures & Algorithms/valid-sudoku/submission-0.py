import numpy as np


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board = np.array(board)
        for i in range(len(board)):
            row = board[i,:]
            if self.has_duplicates(row):
                return False

        for i in range(len(board[0])):
            col = board[:,i]
            if self.has_duplicates(col):
                return False

        for i in range(3):
            for j in range(3):
                box = board[3*i:3*i+3, 3*j:3*j+3]
                if self.has_duplicates(box.flatten()):
                    return False

        return True



    def has_duplicates(self, arr: list[str]) -> bool:
        cache = set()
        for s in arr:
            if s != '.':
                if s in cache:
                    return True
                else:
                    cache.add(s)
    
        return False