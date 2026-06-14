class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows
        for row in board:
            hash_set = set()
            for ch in row:
                if ch.isnumeric():
                    if ch in hash_set:
                        return False
                    else:
                        hash_set.add(ch)
            
        # cols
        for col in range(len(board[0])):
            hash_set = set()
            for row in range(len(board)):
                ch = board[row][col]
                if ch.isnumeric():
                    if ch in hash_set:
                        return False
                    else:
                        hash_set.add(ch)

        # squares
        for i in range(3):
            for j in range(3):
                # get top left index
                row = i * 3
                col = j * 3
                hash_set = set()
                for k in range(3):
                    for l in range(3):
                        r = row + k
                        c = col + l
                        ch = board[r][c]
                        if ch.isnumeric():
                            if ch in hash_set:
                                return False
                            else:
                                hash_set.add(ch)
        
        return True