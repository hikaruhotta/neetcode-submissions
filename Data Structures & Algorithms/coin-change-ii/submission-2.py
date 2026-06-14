class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)

        index = 0
        dp[0] = 1
        for t in range(1, amount + 1):
            if t % coins[index] == 0:
                dp[t] = 1
        
        for index in range(1, len(coins)):
            curr_dp = [0] * (amount + 1)
            curr_dp[0] = 1
            for t in range(1, amount + 1):
                skip = dp[t]

                include = 0
                if coins[index] <= t:
                    include = curr_dp[t - coins[index]]
                
                curr_dp[t] = skip + include
        
            dp = curr_dp
        
        return dp[-1]
