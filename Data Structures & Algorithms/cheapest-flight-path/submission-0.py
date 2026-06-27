import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {i: [] for i in range(n)}
        for flight in flights:
            from_i, to_i, price_i = flight[0], flight[1], flight[2]
            graph[from_i].append((to_i, price_i))
        
        min_heap = []
        visited = set()
        heapq.heappush(min_heap, (0, src, -1)) # (cost, airport, stops)

        while min_heap and len(visited) < n:
            cost, from_i, stops = heapq.heappop(min_heap)
            if from_i in visited:
                continue
            
            if from_i == dst:
                return cost

            if stops == k:
                continue
            
            for neighbor in graph[from_i]:
                (to_i, price_i) = neighbor
                if to_i not in visited:
                    heapq.heappush(min_heap, (cost + price_i, to_i, stops + 1))
        
        return -1





