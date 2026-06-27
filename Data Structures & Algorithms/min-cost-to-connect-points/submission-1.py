import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0

        points = [(point[0], point[1]) for point in points]

        min_heap = []
        visited = set()
        total_cost = 0
        heapq.heappush(min_heap, (0, points[0], None)) # (cost, point, parent)

        while min_heap and len(visited) < len(points):
            cost, point_i, parent_point = heapq.heappop(min_heap)
            if point_i in visited:
                continue
            
            visited.add(point_i)
            total_cost += cost

            for point_j in points:
                if point_j == point_i or point_j == parent_point or point_j in visited:
                    continue
                
                dist = abs(point_i[0] - point_j[0]) + abs(point_i[1] - point_j[1])
                heapq.heappush(min_heap, (dist, point_j, point_i))
        
        return total_cost

        



        