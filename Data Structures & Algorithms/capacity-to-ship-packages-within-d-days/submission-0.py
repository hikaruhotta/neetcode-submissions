class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        L, R = 1, sum(weights)
        result = R
        while L <= R:
            M = L + (R - L) // 2
            if self.canLoad(weights, days, M):
                result = M
                R = M - 1
            else:
                L = M + 1
        return result
    
    def canLoad(self, weights: List[int], max_days: int, capacity: int) -> bool:
        days = 0
        i = 0
        
        while i < len(weights) and days < max_days:
            total_weight = 0
            while i < len(weights) and total_weight + weights[i] <= capacity:
                total_weight += weights[i]
                i += 1

            days += 1
        
        return i == len(weights)
