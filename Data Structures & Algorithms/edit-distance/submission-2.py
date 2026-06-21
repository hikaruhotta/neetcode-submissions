class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        self.word1, self.word2 = word1, word2
        self.cache = {}
        return self.helper(0, 0)

    def helper(self, index1: int, index2: int) -> int:
        if index2 == len(self.word2):
            return len(self.word1) - index1
        elif index1 == len(self.word1):
            return len(self.word2) - index2
        
        if (index1, index2) in self.cache:
            return self.cache[(index1, index2)]
        
        candidates = []
        if self.word1[index1] == self.word2[index2]:
            result = self.helper(index1 + 1, index2 + 1)
            candidates.append(result)
        else:
            insert = 1 + self.helper(index1, index2 + 1)
            delete = 1 + self.helper(index1 + 1, index2)
            replace = 1 + self.helper(index1 + 1, index2 + 1)
            candidates += [insert, delete, replace]

        result = min(candidates)
        self.cache[(index1, index2)] = result
        
        return result
            