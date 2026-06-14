import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        points = [(point[0], point[1]) for point in points]

        totalDist = 0
        visited = set()
        min_heap = []

        visited.add(points[0])
        for i in range(1, len(points)):
            dist = self.manhattanDistance(points[0], points[i])
            heapq.heappush(min_heap, (dist, (points[0], points[i])))
        
        while min_heap:
            dist, (point_i, point_j) = heapq.heappop(min_heap)

            if point_j in visited:
                continue

            visited.add(point_j)
            totalDist += dist

            for i in range(len(points)):
                if points[i] != point_j and points[i] not in visited:
                    heapq.heappush(min_heap, (self.manhattanDistance(point_j, points[i]), (point_j, points[i])))
        
        return totalDist
        
    def manhattanDistance(self, point1, point2) -> int:
        x1, y1 = point1
        x2, y2 = point2
        return abs(y2 - y1) + abs(x2 - x1)