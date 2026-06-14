from collections import defaultdict, deque

class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        in_degrees = [0 for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            in_degrees[v] += 1

        result = []
        queue = deque([i for i in range(n) if in_degrees[i] == 0])

        while queue:
            node = queue.popleft()
            result.append(node)

            for v in adj[node]:
                in_degrees[v] -= 1
                if in_degrees[v] == 0:
                    queue.append(v)

        if len(result) < n:
            return []
        
        return result
