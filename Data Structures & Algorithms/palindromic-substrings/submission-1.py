class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0

        for k in range(len(s)):
            # odd
            i, j = k, k
            while i >= 0 and j < len(s) and s[i] == s[j]:
                result += 1
                i -= 1
                j +=1

            # even
            i, j = k, k + 1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                result += 1
                i -= 1
                j +=1
        
        return result