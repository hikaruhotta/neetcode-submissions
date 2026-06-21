class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0
        if len(t) == len(s):
            return 1 if t == s else 0

        self.cache = {}
        self.s, self.t = s, t
        return self.helper(0, 0)

    def helper(self, si: int, ti: int) -> int:
        if ti == len(self.t):
            return 1
        elif si == len(self.s):
            return 0

        if (si, ti) in self.cache:
            return self.cache[(si, ti)]
        
        result = 0
        if self.s[si] == self.t[ti]:
            result += self.helper(si + 1, ti + 1)
        
        result += self.helper(si + 1, ti)

        self.cache[(si, ti)] = result

        return result


    