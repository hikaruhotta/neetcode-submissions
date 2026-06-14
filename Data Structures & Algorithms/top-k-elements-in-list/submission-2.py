from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        max_heap = []

        buckets = [[] for i in range(len(nums) + 1)]

        for key, val in cnt.items():
            buckets[val].append(key)
        
        result = []

        index = len(nums)

        while index >= 0 and len(result) < k:
            if len(buckets[index]) > k - len(result):
                result += buckets[index][:k - len(result)]
            else:
                result += buckets[index]
            index -= 1
        
        return result

