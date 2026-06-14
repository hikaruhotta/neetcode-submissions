class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.text1 = text1
        self.text2 = text2
        self.cache = {}
        return self.dfs(0, 0)
    
    def dfs(self, text1_index, text2_index) -> int:
        if text1_index == len(self.text1) or text2_index == len(self.text2):
            return 0

        if (text1_index, text2_index) in self.cache:
            return self.cache[(text1_index, text2_index)]

        if self.text1[text1_index] == self.text2[text2_index]:
            result = 1 + self.dfs(text1_index + 1, text2_index + 1)
            self.cache[(text1_index, text2_index)] = result
            return result
        
        candidates = []
        
        candidates.append(self.dfs(text1_index + 1, text2_index))
        candidates.append(self.dfs(text1_index, text2_index + 1))

        result = max(candidates)
        self.cache[(text1_index, text2_index)] = result
        return result