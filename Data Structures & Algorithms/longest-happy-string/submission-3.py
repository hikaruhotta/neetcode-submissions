import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        if a > 0:
            heapq.heappush(max_heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(max_heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(max_heap, (-c, 'c'))

        result = ""
        if not max_heap:
            return result
        (neg_freq, ch) = heapq.heappop(max_heap)
        result += ch
        next_freq = -neg_freq - 1
        if next_freq > 0:
            heapq.heappush(max_heap, (-next_freq, ch))

        while max_heap:
            tmp = None
            if len(result) >= 2 and max_heap[0][1] == result[-1] and max_heap[0][1] == result[-2]:
                (neg_freq, ch) = heapq.heappop(max_heap)
                tmp = (neg_freq, ch)
            if not max_heap:
                break
            (neg_freq, ch) = heapq.heappop(max_heap)
            result += ch
            next_freq = -neg_freq - 1
            if next_freq > 0:
                heapq.heappush(max_heap, (-next_freq, ch))
            
            if tmp:
                heapq.heappush(max_heap, tmp)
        
        return result
            

            