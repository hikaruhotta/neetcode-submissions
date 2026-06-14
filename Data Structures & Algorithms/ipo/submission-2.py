import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        capital_min_heap = []
        for i, cap in enumerate(capital):
            heapq.heappush(capital_min_heap, (cap, i))

        profit_max_heap = []

        for _ in range(k):
            while capital_min_heap and capital_min_heap[0][0] <= w:
                (cap, i) = heapq.heappop(capital_min_heap)
                heapq.heappush(profit_max_heap, (-profits[i], i))
            
            if profit_max_heap:
                neg_profit, i = heapq.heappop(profit_max_heap)
                w += -neg_profit
        
        return w