class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        self.s, self.t = s, t
        self.cache = {}

        return self.helper(0, 0)
    
    def helper(self, i: int, j: int) -> int:
        if i >= len(self.s) or j >= len(self.t):
            return 1 if j >= len(self.t) else 0

        if (i, j) in self.cache:
            return self.cache[(i, j)]
        
        result = 0
        if self.s[i] == self.t[j]:
            result += self.helper(i + 1, j + 1)
        
        result += self.helper(i + 1, j)

        self.cache[(i, j)] = result

        return result

        
