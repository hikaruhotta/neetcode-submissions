class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [0 for col in range(len(obstacleGrid[0]))]
        row = 0
        dp[0] = 1 if obstacleGrid[0][0] == 0 else 0
        for col in range(1, len(obstacleGrid[0])):
            if dp[col - 1] == 1 and obstacleGrid[row][col] == 0:
                dp[col] = 1
        
        for row in range(1, len(obstacleGrid)):
            next_dp = [0 for col in range(len(obstacleGrid[0]))]
            if obstacleGrid[row][0] == 0:
                next_dp[0] = dp[0]
            for col in range(1, len(obstacleGrid[0])):
                if obstacleGrid[row][col] == 0:
                    next_dp[col] = next_dp[col - 1] + dp[col]
            dp = next_dp
        return dp[-1]
            