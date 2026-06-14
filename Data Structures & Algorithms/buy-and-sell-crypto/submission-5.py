class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prices_to_right = []

        curr_max = None
        for i in reversed(range(len(prices))):
            if curr_max is None or prices[i] > curr_max:
                curr_max = prices[i]
            max_prices_to_right.append(curr_max)
        
        max_prices_to_right = max_prices_to_right[::-1]
        
        max_profits = [max_prices_to_right[i] - prices[i] for i in range(len(prices))]

        return max(max_profits)
            

        