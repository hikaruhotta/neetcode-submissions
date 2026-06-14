import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = [(self.distance(point), point) for point in points]
        heapq.heapify(min_heap)

        result = []
        for i in range(k):
            distance, point = heapq.heappop(min_heap)
            result.append(point)
        return result


    def distance(self, point: List[int]):
        x_i, y_i = point[0], point[1]
        return (x_i**2 + y_i**2)**0.5
