class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = set(coins)

        dp = [0] + [float('inf')] * amount

        for val in range(1, amount + 1):
            candidates = []
            
            for coin in coins:
                if val - coin >= 0:
                    candidates.append(dp[val - coin] + 1)
            
            if candidates:
                dp[val] = min(candidates)

        if dp[amount] == float('inf'):
            return -1
        
        return dp[amount]



