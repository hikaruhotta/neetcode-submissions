from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        max_heap = []

        for task, freq in cnt.items():
            heapq.heappush(max_heap, (-freq, task))

        min_heap = []

        cycles = 0

        while max_heap or min_heap:
            while min_heap and min_heap[0][0] <= cycles:
                (min_cycles, freq, task) = heapq.heappop(min_heap)
                heapq.heappush(max_heap, (-freq, task))

            if max_heap:
                (neg_freq, task) = heapq.heappop(max_heap)
                freq = -neg_freq
                
                if freq - 1 > 0:
                    heapq.heappush(min_heap, (cycles + n + 1, freq - 1, task))
            
            cycles += 1
        
        return cycles




            


            




