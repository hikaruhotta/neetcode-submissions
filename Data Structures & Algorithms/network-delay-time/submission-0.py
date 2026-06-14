from collections import deque

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i: [] for i in range(1, n + 1)}
        for ui, vi, ti in times:
            graph[ui].append((vi, ti))
        
        result = {i: float('inf') for i in range(1, n + 1)}

        queue = deque([(k, 0)])

        while queue:
            node, curr_time = queue.pop()
            result[node] = min(curr_time, result[node])

            for adj_node, signal_time in graph[node]:
                if result[adj_node] > curr_time + signal_time:
                    queue.append((adj_node, curr_time + signal_time))
        
        max_result = max(result.values())
        if max_result == float('inf'):
            return -1
        else:
            return max_result
            



        

