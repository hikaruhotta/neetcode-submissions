class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if (len(s1) + len(s2))!= len(s3):
            return False

        self.s1, self.s2, self.s3 = s1, s2, s3
        self.cache = {}

        return self.helper(0, 0, 0)

    def helper(self, i: int, j: int, k: int) -> bool:
        if i >= len(self.s1):
            return self.s2[j:] == self.s3[k:]
        elif j >= len(self.s2):
            return self.s1[i:] == self.s3[k:]

        if (i, j, k) in self.cache:
            return self.cache[(i, j, k)]
        
        result = False

        if self.s1[i] == self.s3[k]:
            result = result or self.helper(i + 1, j, k + 1)
        if self.s2[j] == self.s3[k]:
            result = result or self.helper(i, j + 1, k + 1)

        self.cache[(i, j, k)] = result
        
        return result









        
