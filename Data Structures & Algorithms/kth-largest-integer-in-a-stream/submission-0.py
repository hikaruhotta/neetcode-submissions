import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [num for num in nums]
        heapq.heapify(self.heap)
        self.k = k
        self.popping()

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        self.popping()
        return self.heap[0]

    def popping(self):
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
