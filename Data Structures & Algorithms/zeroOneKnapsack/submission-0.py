class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # row = item, col = capacity
        dp = [[0 for _ in range(capacity + 1)] for _ in range(len(weight))]

        item = 0
        for cap in range(capacity + 1):
            if cap >= weight[item]:
                dp[item][cap] = profit[item]
        
        cap = 0
        for item in range(len(weight)):
            dp[item][cap] = 0
        
        for item in range(1, len(weight)):
            for cap in range(1, capacity + 1):
                skip = dp[item - 1][cap]

                include = 0
                if weight[item] <= cap:
                    include = profit[item] + dp[item - 1][cap - weight[item]]
                
                dp[item][cap] = max(skip, include)

        print(dp)
        
        return dp[-1][-1]
