class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        self.word1, self.word2 = word1, word2
        self.cache = {}

        return self.helper(0, 0)
    
    def helper(self, i: int, j: int) -> int:
        if i >= len(self.word1) and j >= len(self.word2):
            return 0
        elif i < len(self.word1) and j >= len(self.word2):
            return len(self.word1) - i
        elif i >= len(self.word1) and j < len(self.word2):
            return len(self.word2) - j

        if (i, j) in self.cache:
            return self.cache[(i, j)]
        

        if self.word1[i] == self.word2[j]:
            result = self.helper(i + 1, j + 1)
        else:
            result = 1 + min(
                self.helper(i + 1, j), self.helper(i, j + 1), self.helper(i + 1, j + 1)
            )
        
        self.cache[(i, j)] = result
        
        return result

