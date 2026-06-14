class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = [float('inf') for i in range(len(cost) + 1)]

        for i in range(len(min_cost)):
            if i == 0 or i == 1:
                min_cost[i] = cost[i]
            elif i == len(cost):
                min_cost[i] = min(min_cost[i - 1], min_cost[i - 2])
            else:
                min_cost[i] = cost[i] + min(min_cost[i - 1], min_cost[i - 2])
        
        return min_cost[-1]
