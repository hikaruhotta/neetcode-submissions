class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1 for i in range(n)]
        for row in range(1, m):
            next_dp = [0 for i in range(n)]
            next_dp[0] = 1
            for col in range(1, n):
                next_dp[col] = next_dp[col - 1] + dp[col]
            dp = next_dp
        return dp[-1]
