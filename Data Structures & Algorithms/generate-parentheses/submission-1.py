class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []
        self.helper('(', 1, 0, n)
        return self.result
    
    def helper(self, seq: str, num_open: int, num_close: int, n: int) -> None:
        if num_open == num_close and num_open == n:
            self.result.append(seq)
            return
        
        if num_open < n:
            seq += '('
            self.helper(seq, num_open + 1, num_close, n)
            seq = seq[:-1]
        
        if num_close < num_open:
            seq += ')'
            self.helper(seq, num_open, num_close + 1, n)
            seq = seq[:-1]