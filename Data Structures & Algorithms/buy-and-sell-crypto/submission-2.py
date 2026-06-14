class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_to_right = [0]
        for i in reversed(range(len(prices) - 1)):
            max_to_right.append(max(prices[i + 1], max_to_right[-1]))
        max_to_right = max_to_right[::-1]

        result = 0
        for i in range(len(prices)):
            result = max(result, max_to_right[i] - prices[i])
        return result
        

