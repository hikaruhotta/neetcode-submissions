from collections import deque

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        graph = {i: [] for i in range(1, N + 1)}
        indegree = {i: 0 for i in range(1, N + 1)}

        for edge in edges:
            a, b = edge[0], edge[1]
            graph[a].append(b)
            indegree[b] += 1
            graph[b].append(a)
            indegree[a] += 1
        
        queue = deque([])
        for key, val in indegree.copy().items():
            if val <= 1:
                queue.append(key)
                del indegree[key]
        
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor in indegree:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] <= 1:
                        queue.append(neighbor)
                        del indegree[neighbor]
        
        result = None
        for edge in edges:
            if edge[0] in indegree and edge[1] in indegree:
                result = edge
        
        return result


        

