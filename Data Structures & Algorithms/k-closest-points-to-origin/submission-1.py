import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        heapq.heapify(max_heap)

        for point in points:
            heapq.heappush(max_heap, (-self.distance(point), point))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        


        return [point for neg_distance, point in max_heap]


    def distance(self, point: List[int]):
        x_i, y_i = point[0], point[1]
        return (x_i**2 + y_i**2)**0.5
