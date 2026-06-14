class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.prices = prices
        self.cache = {}
        return self.dfs(0, True)

    def dfs(self, day: int, is_buying: int) -> int:
        if day >= len(self.prices):
            return 0

        if (day, is_buying) in self.cache:
            return self.cache[(day, is_buying)]

        candidates = []

        if is_buying:
            # buy today
            candidates.append(self.dfs(day + 1, False) - self.prices[day])

            # skip buying today
            candidates.append(self.dfs(day + 1, True))
        
        else:
            # sell today
            candidates.append(self.dfs(day + 2, True) + self.prices[day])

            # skip selling today
            candidates.append(self.dfs(day + 1, False))
        
        result = max(candidates)
        self.cache[(day, is_buying)] = result
        return result



        


      




        

        
