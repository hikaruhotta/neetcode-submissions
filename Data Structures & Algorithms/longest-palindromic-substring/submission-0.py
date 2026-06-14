class Solution:
    def longestPalindrome(self, s: str) -> str:
        cache = {}
        result = ""

        for i, ch in enumerate(s):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if len(s[left : right + 1]) > len(result):
                    result = s[left : right + 1]
                left -= 1
                right += 1

        for i, ch in enumerate(s):
            if i == len(s) - 1:
                continue

            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if len(s[left : right + 1]) > len(result):
                    result = s[left : right + 1]
                left -= 1
                right += 1
        
        return result