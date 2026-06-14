from collections import Counter
import heapq  

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        min_heap = []
        for num, cnt in counter.items():
            heapq.heappush(min_heap, (cnt, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return [num for cnt, num in min_heap]
            
