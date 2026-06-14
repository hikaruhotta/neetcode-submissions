class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)

        dp = [True] + [False] * len(s)

        for i in range(len(s) + 1):
            if dp[i]:
                for word in wordDict:
                    if i + len(word) <= len(s):
                        if s[i : i + len(word)] == word:
                            dp[i + len(word)] = True
        
        return dp[-1]
        

