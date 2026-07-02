class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i1, i2 = 0, 0
        result = ""

        while i1 < len(word1) and i2 < len(word2):
            result += word1[i1]
            result += word2[i2]
            i1 += 1
            i2 += 1
        
        if i1 < len(word1):
            result += word1[i1:]
        elif i2 < len(word2):
            result += word2[i2:]
        
        return result
