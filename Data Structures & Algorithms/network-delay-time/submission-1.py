import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for ui, vi, ti in times:
            if ui not in adj:
                adj[ui] = []
            adj[ui].append((vi, ti))

        min_adj_times = {}
        min_heap = [(0, k)]

        while min_heap and len(min_adj_times) < n:
            c, u = heapq.heappop(min_heap)
            if u in min_adj_times:
                continue
            min_adj_times[u] = c

            if u in adj:
                for vi, ti in adj[u]:
                    if vi in min_adj_times:
                        continue
                    heapq.heappush(min_heap, (c + ti, vi))

        if len(min_adj_times) != n:
            return -1
        
        return max(min_adj_times.values())
