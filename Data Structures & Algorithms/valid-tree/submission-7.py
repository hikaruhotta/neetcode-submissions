from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        graph = {i: [] for i in range(n)}

        for edge in edges:
            a, b = edge[0], edge[1]
            graph[a].append(b)
            graph[b].append(a)
        
        # detect cycle
        visited = set()
        queue = deque([(0, None)])

        while queue:
            node, parent = queue.popleft()
            if node in visited:
                return False
            visited.add(node)

            for neighbor in graph[node]:
                if parent != neighbor:
                    queue.append((neighbor, node))
        
        return len(visited) == n

