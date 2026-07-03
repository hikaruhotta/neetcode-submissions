import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        min_heap = []
        for num in arr:
            heapq.heappush(min_heap, (abs(x - num), num))
        
        min_heap_result = []
        for _ in range(k):
            if min_heap:
                delta, num = heapq.heappop(min_heap)
                heapq.heappush(min_heap_result, num)
        
        result = []
        while min_heap_result:
            num = heapq.heappop(min_heap_result)
            result.append(num)

        return result
        