class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]

        for row in range(m):
            for col in range(n):
                if row == 0 and col == 0:
                    dp[row][col] = 1

                for i, j in [(-1, 0), (0, -1)]:
                    prior_row, prior_col = row + i, col + j
                    if self.inbounds(m, n, prior_row, prior_col):
                        dp[row][col] += dp[prior_row][prior_col]
        
        return dp[m - 1][n - 1]

    
    def inbounds(self, m, n, row, col):
        return row >= 0 and row < m and col >= 0 and col < n