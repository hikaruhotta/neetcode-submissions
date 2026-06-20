class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.text1, self.text2 = text1, text2
        self.cache = {}
        return self.helper(0, 0)
        
    def helper(self, index1: int, index2: int) -> int:
        if index1 == len(self.text1) or index2 == len(self.text2):
            return 0
        
        if (index1, index2) in self.cache:
            return self.cache[(index1, index2)]

        candidates = []
        if self.text1[index1] == self.text2[index2]:
            candidates.append(1 + self.helper(index1 + 1, index2 + 1))
        
        candidates.append(self.helper(index1 + 1, index2))
        candidates.append(self.helper(index1, index2 + 1))

        result = max(candidates)
        self.cache[(index1, index2)] = result
        return result