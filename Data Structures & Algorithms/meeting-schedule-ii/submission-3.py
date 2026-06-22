"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals = [(interval.start, interval.end) for interval in intervals]
        intervals = sorted(intervals, key=lambda x: x[0])

        result = 0
        min_heap = []
        for interval in intervals:
            while min_heap and min_heap[0][0] <= interval[0]:
                heapq.heappop(min_heap)
            
            heapq.heappush(min_heap, (interval[1], interval))
            result = max(result, len(min_heap))

        return result



