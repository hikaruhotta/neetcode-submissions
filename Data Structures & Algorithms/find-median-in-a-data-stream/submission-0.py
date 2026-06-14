import heapq

class MedianFinder:

    def __init__(self):
        self.small = [] # max heap
        self.large = [] # min heap

    def addNum(self, num: int) -> None:
        # push to small
        heapq.heappush(self.small, -num)

        # if max of small > min of large, swap
        if self.small and self.large and -self.small[0] > self.large[0]:
            popped_num = -heapq.heappop(self.small)
            heapq.heappush(self.large, popped_num)

        # balance small and large
        if len(self.small) > len(self.large) + 1:
            popped_num = heapq.heappop(self.small)
            heapq.heappush(self.large, -popped_num)
        elif len(self.large) > len(self.small) + 1:
            popped_num = heapq.heappop(self.large)
            heapq.heappush(self.small, -popped_num)

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        elif len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return self.large[0]
        
        