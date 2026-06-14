class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_to_right = []

        curr_max = None
        for i in reversed(range(len(prices))):
            price = prices[i]
            if curr_max is None:
                curr_max = price
            else:
                curr_max = max(curr_max, price)
            max_to_right.append(curr_max)

        max_to_right = max_to_right[::-1]
        
        max_profit = 0
        for i in range(len(prices)):
            profit = max_to_right[i] - prices[i]
            max_profit = max(max_profit, profit)
        
        return max_profit

