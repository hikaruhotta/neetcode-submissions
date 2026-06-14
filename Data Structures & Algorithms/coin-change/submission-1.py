class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        index = 0
        for t in range(1, amount + 1):
            if t % coins[index] == 0:
                dp[t] = t // coins[index]
        
        for index in range(1, len(coins)):
            next_dp = [float('inf')] * (amount + 1)
            next_dp[0] = 0
            for t in range(1, amount + 1):
                skip = dp[t]

                include = float('inf')
                if coins[index] <= t:
                    include = 1 + next_dp[t - coins[index]]
                
                next_dp[t] = min(skip, include)
        
            dp = next_dp
        
        if dp[-1] == float('inf'):
            return -1
        
        return dp[-1]



