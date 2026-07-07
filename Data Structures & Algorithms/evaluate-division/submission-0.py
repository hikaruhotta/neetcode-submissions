from collections import deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        for i in range(len(equations)):
            a, b = equations[i][0], equations[i][1]
            value = values[i]
            if a not in graph:
                graph[a] = []
            graph[a].append((b, value))
            if b not in graph:
                graph[b] = []
            graph[b].append((a, 1.0 / value))
        
        results = []
        for query in queries:
            results.append(self.helper(graph, query))
        return results
    
    def helper(self, graph: Dict, query: List[str]) -> float:
        c, d = query[0], query[1]

        if c not in graph or d not in graph:
            return -1.0

        queue = deque([(c, 1)])
        visited = set([c])

        while queue:
            node, answer = queue.popleft()
            if node == d:
                return answer
            
            if node in graph:
                for neighbor, val in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, answer * val))
        
        return -1.0


        