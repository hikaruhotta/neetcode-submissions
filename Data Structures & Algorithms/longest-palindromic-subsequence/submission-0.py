class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        self.cache = {}
        return self.helper(s, 0, len(s) - 1)
    
    def helper(self, s: str, i: int, j: int) -> int:
        if i == j:
            return 1
        elif j < i:
            return 0

        if (i, j) in self.cache:
            return self.cache[(i, j)]
        
        if s[i] == s[j]:
            result = 2 + self.helper(s, i + 1, j - 1)
        else:
            result = max(self.helper(s, i + 1, j), self.helper(s, i, j - 1))

        self.cache[(i, j)] = result

        return result
        
        
