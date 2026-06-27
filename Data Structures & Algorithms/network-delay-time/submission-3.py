import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i: [] for i in range(1, n + 1)}
        for ui, vi, ti in times:
            graph[ui].append((vi, ti))
        
        min_heap = []
        visited = set([k])
        time = 0
        for vi, ti in graph[k]:
            heapq.heappush(min_heap, (0 + ti, vi)) 
        
        while min_heap and len(visited) < n:
            ti, vi = heapq.heappop(min_heap)
            if vi not in visited:
                time = max(time, ti)
                visited.add(vi)
                for vj, tj in graph[vi]:
                    if vj not in visited:
                        heapq.heappush(min_heap, (ti + tj, vj))
            
        if len(visited) < n:
            return -1
        
        return time
        
