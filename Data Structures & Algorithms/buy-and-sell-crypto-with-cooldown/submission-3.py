class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.prices = prices
        self.cache = {}
        return self.helper(0)

    def helper(self, index: int) -> int:
        if index >= len(self.prices):
            return 0

        if index in self.cache:
            return self.cache[index]

        candidates = []

        # dont buy on day index
        candidates.append(self.helper(index + 1))
        
        # buy
        for sell_index in range(index + 1, len(self.prices)):
            result = self.prices[sell_index] - self.prices[index] + self.helper(sell_index + 2)
            candidates.append(result)
        
        result = max(candidates)

        self.cache[index] = result
        return result

        
        
