import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        max_heap = []
        cnt = Counter(s)

        for ch, freq in cnt.items():
            heapq.heappush(max_heap, (-freq, ch))
        
        
        (neg_freq, ch) = heapq.heappop(max_heap)
        result = ch

        new_freq = -neg_freq - 1
        if new_freq > 0:
            heapq.heappush(max_heap, (-new_freq, ch))

        while max_heap:
            tmp = []
            while max_heap[0][1] == result[-1]:
                (neg_freq, ch) = heapq.heappop(max_heap)
                tmp.append((neg_freq, ch))
                if not max_heap:
                    return ""
            (neg_freq, ch) = heapq.heappop(max_heap)
            result += ch
            new_freq = -neg_freq - 1
            if new_freq > 0:
                heapq.heappush(max_heap, (-new_freq, ch))
            for (neg_freq, ch) in tmp:
                heapq.heappush(max_heap, (neg_freq, ch))

        return result


