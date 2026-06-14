class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = s[0]

        for k in range(len(s)):
            # odd length
            i, j = k, k
            while i >= 0 and j < len(s) and s[i] == s[j]:
                result = s[i : j + 1] if len(result) < j - i + 1 else result
                i -= 1
                j += 1

            # even length
            i, j = k, k + 1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                result = s[i: j + 1] if len(result) < j - i + 1 else result
                i -= 1
                j += 1
            
        return result
