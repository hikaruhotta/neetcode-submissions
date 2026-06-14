import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []

        max_heap = []

        for i in range(k):
            heapq.heappush(max_heap, (-nums[i], i))
        
        result.append(-max_heap[0][0])

        for i in range(1, len(nums) - k + 1):
            heapq.heappush(max_heap, (-nums[i + k - 1], i + k - 1))
        
            while max_heap[0][1] < i:
                heapq.heappop(max_heap)
            
            result.append(-max_heap[0][0])
        
        return result
            
