import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = [(-num, i) for i, num in enumerate(nums[:k])]
        heapq.heapify(max_heap)

        results = [-max_heap[0][0]]

        for i in range(1, len(nums) - k + 1):
            while len(max_heap) > 0 and max_heap[0][1] < i:
                heapq.heappop(max_heap)
            heapq.heappush(max_heap, (-nums[i + k - 1], i + k - 1))
            results.append(-max_heap[0][0])

        return results

