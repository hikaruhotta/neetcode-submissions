class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""

        dp = [[False] * len(s) for _ in range(len(s))]

        # n -> 0
        for i in range(len(s) - 1, -1, -1):
            # i -> 0
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i <= 2 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        if j - i + 1 >= len(result):
                            result = s[i : j + 1]
        
        return result
                        

                



