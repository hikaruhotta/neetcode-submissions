from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        max_heap = []

        for key, val in cnt.items():
            heapq.heappush(max_heap, (-val, key))

        result = []
        for i in range(k):
            _, num = heapq.heappop(max_heap)
            result.append(num)
        
        return result

