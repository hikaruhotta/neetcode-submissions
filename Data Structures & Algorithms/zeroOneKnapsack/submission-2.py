class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # row = item, col = capacity
        dp = [0 for _ in range(capacity + 1)]

        item = 0
        for cap in range(capacity + 1):
            if cap >= weight[item]:
                dp[cap] = profit[item]
        
        for item in range(1, len(weight)):
            next_dp = [0 for _ in range(capacity + 1)]
            for cap in range(1, capacity + 1):
                skip = dp[cap]

                include = 0
                if weight[item] <= cap:
                    include = profit[item] + dp[cap - weight[item]]
                
                next_dp[cap] = max(skip, include)
            
            dp = next_dp

        return dp[-1]
