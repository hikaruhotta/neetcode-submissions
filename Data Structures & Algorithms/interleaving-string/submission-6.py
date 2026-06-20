class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        self.s1, self.s2, self.s3 = s1, s2, s3

        self.cache = {}
        return self.helper(0, 0)

    def helper(self, index1: int, index2: int) -> bool:
        index3 = index1 + index2
        if index3 == len(self.s3):
            return True
        if index1 == len(self.s1):
            return self.s2[index2:] == self.s3[index3:]
        if index2 == len(self.s2):
            return self.s1[index1:] == self.s3[index3:]

        if (index1, index2) in self.cache:
            return self.cache[(index1, index2)]

        candidates = []
        if self.s1[index1] == self.s3[index3]:
            candidates.append(self.helper(index1 + 1, index2))
        if self.s2[index2] == self.s3[index3]:
            candidates.append(self.helper(index1, index2 + 1))

        result = any(candidates)
        self.cache[(index1, index2)] = result
        
        return result
