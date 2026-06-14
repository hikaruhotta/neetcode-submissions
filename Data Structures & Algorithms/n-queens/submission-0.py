class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.results = []
        self.helper(n, 0, [])
        final = []

        for result in self.results:
            res = []
            for (row, col) in result:
                res.append(''.join(['Q' if i == col else '.' for i in range(n)]))
            final.append(res)

        return final

    def helper(self, n: int, row: int, seq: List) -> None:
        if row == n:
            self.results.append(seq.copy())
            return
        
        for col in range(n):
            if self.isValid(row, col, seq):
                seq.append((row, col))
                self.helper(n, row + 1, seq)
                seq.pop()

    def isValid(self, row: int, col: int, seq: List) -> bool:
        if len(seq) == 0:
            return True

        for (x, y) in seq:
            if row == x or col == y:
                return False

            if abs(row - x) == abs(col - y):
                return False
        
        return True
        




    