import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = {}
        for i, (u, v) in enumerate(edges):
            if u not in adj:
                adj[u] = []
            if v not in adj:
                adj[v] = []
            adj[u].append((succProb[i], v))
            adj[v].append((succProb[i], u))
        
        res_probs = {}

        max_heap = [(-1, start_node)]

        while max_heap:
            curr_prob, curr_node = heapq.heappop(max_heap)
            curr_prob = curr_prob * -1 

            if curr_node in res_probs:
                continue

            res_probs[curr_node] = curr_prob

            if curr_node in adj:
                for prob, v in adj[curr_node]:
                    heapq.heappush(max_heap, (-curr_prob * prob, v))
        
        if end_node in res_probs:
            return res_probs[end_node]
        
        return 0



