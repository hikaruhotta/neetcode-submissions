class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        for i in range(len(s)):
            L, R = i, i
            while L >= 0 and R < len(s) and s[L] == s[R]:
                if R - L + 1 > len(result):
                    result = s[L : R + 1]
                L -= 1
                R += 1
        
        if len(s) >= 2:
            for i in range(len(s) - 1):
                L, R = i, i + 1
                while L >= 0 and R < len(s) and s[L] == s[R]:
                    if R - L + 1 > len(result):
                        result = s[L : R + 1]
                    L -= 1
                    R += 1
        return result
