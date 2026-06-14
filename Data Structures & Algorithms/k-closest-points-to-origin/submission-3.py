import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for x, y in points:
            dist = x**2 + y **2
            heapq.heappush(max_heap, (-dist, [x, y]))
            while len(max_heap) > k:
                heapq.heappop(max_heap)
        
        return [point for eng_dist, point in max_heap]