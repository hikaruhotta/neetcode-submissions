class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.prices = prices
        self.cache = {}
        return self.dfs(0, -2)

    def dfs(self, day: int, day_last_sold: int) -> int:
        if day == len(self.prices):
            return 0

        if (day, day_last_sold) in self.cache:
            return self.cache[(day, day_last_sold)]
        
        candidates = []

        # 1. Don't buy today, skip to next day
        candidates.append(self.dfs(day + 1, day_last_sold))

        # 2 Buy today, find sell day candidate
        if day - day_last_sold > 1:
            for sell_day in range(day + 1, len(self.prices)):
                if self.prices[sell_day] >= self.prices[day]:
                    candidates.append(self.prices[sell_day] - self.prices[day] + self.dfs(sell_day + 1, sell_day))
        result = max(candidates)
        self.cache[(day, day_last_sold)] = result
        return result




        

        
