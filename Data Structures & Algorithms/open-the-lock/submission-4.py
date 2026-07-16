import heapq

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if '0000' in deadends:
            return -1

        min_heap = []
        heapq.heappush(min_heap, (0, '0000'))
        visited = set()

        while min_heap:
            turns, comb = heapq.heappop(min_heap)
            if comb in visited:
                continue
            visited.add(comb)
            if comb == target:
                return turns
            
            for i in range(4):
                next_comb = comb[:i] + str((int(comb[i]) + 1) % 10) + comb[i + 1:]
                if next_comb not in deadends and next_comb not in visited:
                    heapq.heappush(min_heap, (turns + 1, next_comb))
                
                prev_comb = comb[:i] + str((int(comb[i]) - 1 + 10) % 10) + comb[i + 1:]
                if prev_comb not in deadends and prev_comb not in visited:
                    heapq.heappush(min_heap, (turns + 1, prev_comb))
        
        return -1
