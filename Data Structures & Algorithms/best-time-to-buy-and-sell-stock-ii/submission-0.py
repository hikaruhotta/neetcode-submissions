class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.prices = prices
        self.cache = {}
        return self.helper(0, True)
        
    def helper(self, index: int, can_buy: bool) -> int:
        if index == len(self.prices):
            return 0
        
        if (index, can_buy) in self.cache:
            return self.cache[(index, can_buy)]
        
        candidates = []
        if can_buy:
            candidates.append(self.helper(index + 1, False) - self.prices[index])
        else:
            candidates.append(self.helper(index + 1, True) + self.prices[index])
        
        candidates.append(self.helper(index + 1, can_buy))

        result = max(candidates)
        self.cache[(index, can_buy)] = result

        return result

        


