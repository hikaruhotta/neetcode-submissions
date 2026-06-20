class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            res = float('inf')
            for coin in coins:
                if i - coin >= 0 and dp[i - coin] != -1:
                    res = min(res, dp[i - coin] + 1)
            if res != float('inf'):
                dp[i] = res
        print(dp)
        return dp[-1]