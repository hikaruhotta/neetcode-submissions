import heapq

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[0])

        max_heap = []

        for interval in intervals:
            should_push = True
            while max_heap and max_heap[0][1][1] > interval[0]:
                if max_heap[0][1][1] == interval[1]:
                    if interval[0] < max_heap[0][1][0]:
                        heapq.heappop(max_heap)
                    else:
                        should_push = False
                        break
                elif max_heap[0][1][1] > interval[1]:
                    heapq.heappop(max_heap)
                else:
                    should_push = False
                    break
            if should_push:
                heapq.heappush(max_heap, (-interval[1], (interval[0], interval[1])))
        return len(intervals) - len(max_heap)
                    



