import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        enqueue_min_heap = []
        processing_min_heap = []

        for i, task in enumerate(tasks):
            enqueue_time_i, processing_time_i = task[0], task[1]
            heapq.heappush(enqueue_min_heap, (enqueue_time_i, processing_time_i, i))
        
        result = []
        
        time = 0
        while enqueue_min_heap or processing_min_heap:
            while enqueue_min_heap and enqueue_min_heap[0][0] <= time:
                (enqueue_time_i, processing_time_i, i) = heapq.heappop(enqueue_min_heap)
                heapq.heappush(processing_min_heap, (processing_time_i, i))
            if processing_min_heap:
                (processing_time_i, i) = heapq.heappop(processing_min_heap)
                result.append(i)
                time += processing_time_i
            else:
                time = enqueue_min_heap[0][0]
        
        return result
            


