class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [0 for col in range(len(grid[0]))]
        dp[0] = grid[0][0]
        for col in range(1, len(grid[0])):
            dp[col] = dp[col - 1] + grid[0][col]
        
        for row in range(1, len(grid)):
            next_dp = [0 for col in range(len(grid[0]))]
            next_dp[0] = dp[0] + grid[row][0]
            for col in range(1, len(grid[0])):
                next_dp[col] = min(dp[col], next_dp[col - 1]) + grid[row][col]
            dp = next_dp
        
        return dp[-1]