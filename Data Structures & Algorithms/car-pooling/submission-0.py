import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        scheduled_min_heap = []
        for trip in trips:
            num_passengers_i, from_i, to_i = trip[0], trip[1], trip[2]
            heapq.heappush(scheduled_min_heap, (from_i, to_i, num_passengers_i))
        
        active_min_heap = []

        position, num_passengers = 0, 0

        while scheduled_min_heap:
            (from_i, to_i, num_passengers_i) = heapq.heappop(scheduled_min_heap)

            while active_min_heap and active_min_heap[0][0] <= from_i:
                to_j, num_passengers_j = heapq.heappop(active_min_heap)
                num_passengers -= num_passengers_j
            
            if num_passengers + num_passengers_i > capacity:
                return False
            
            num_passengers += num_passengers_i
            heapq.heappush(active_min_heap, (to_i, num_passengers_i))
        
        return True
            