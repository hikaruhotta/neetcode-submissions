class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N, M = len(text1), len(text2)

        dp = [0 for _ in range(M + 1)]

        for i in range(N):
            curr_dp = [0 for _ in range(M + 1)]
            for j in range(M):
                if text1[i] == text2[j]:
                    curr_dp[j + 1] = 1 + dp[j]
                else:
                    curr_dp[j + 1] = max(dp[j + 1], curr_dp[j])
            
            dp = curr_dp
        
        return dp[-1]