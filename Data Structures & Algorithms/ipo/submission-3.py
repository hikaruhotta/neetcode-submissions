import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        capital_min_heap = []
        for i in range(len(profits)):
            heapq.heappush(capital_min_heap, (capital[i], profits[i]))

        delta_max_heap = []

        for i in range(k):
            while capital_min_heap and capital_min_heap[0][0] <= w:
                (capital_i, profits_i) = heapq.heappop(capital_min_heap)
                heapq.heappush(delta_max_heap, -profits_i)
            
            if not delta_max_heap:
                return w
            
            neg_profits_i = heapq.heappop(delta_max_heap)
            profits_i = -neg_profits_i
            w += profits_i
        
        return w



