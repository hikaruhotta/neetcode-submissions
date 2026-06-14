import heapq

class MedianFinder:

    def __init__(self):
        self.max_heap, self.min_heap = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)
        if self.min_heap and -self.max_heap[0] > self.min_heap[0]:
            popped_neg_num = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -popped_neg_num)
        
        if len(self.min_heap) > len(self.max_heap) + 1:
            popped_num = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -popped_num)
        elif len(self.max_heap) > len(self.min_heap) + 1:
            neg_popped_num = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -neg_popped_num)


    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return float(-self.max_heap[0] + self.min_heap[0]) / 2
        elif len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return self.min_heap[0]
        
        