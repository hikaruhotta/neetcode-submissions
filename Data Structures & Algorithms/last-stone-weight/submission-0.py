import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        negative_stones = [-weight for weight in stones]
        heapq.heapify(negative_stones)
        while len(negative_stones) >= 2:
            x = -heapq.heappop(negative_stones)
            y = -heapq.heappop(negative_stones)
            if x == y:
                continue
            elif x < y:
                heapq.heappush(negative_stones, -(y - x))
            else:
                heapq.heappush(negative_stones, -(x - y))


        if len(negative_stones) == 1:
            return -negative_stones[0]
        else:
            return 0

        

