from collections import Counter
import heapq
from collections import deque


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)

        max_heap = [-val for key, val in freq.items()]
        heapq.heapify(max_heap)

        queue = deque()

        time = 0

        while max_heap or len(queue) > 0:
            if len(queue) > 0:
                neg_freq, can_push_time = queue[0]
                if can_push_time <= time:
                    queue.popleft()
                    heapq.heappush(max_heap, neg_freq)

            time += 1
            if max_heap:
                neg_freq = heapq.heappop(max_heap)
                if neg_freq + 1 != 0:
                    queue.append((neg_freq + 1, time + n))

        return time





        