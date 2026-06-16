from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        for edge in edges:
            a, b = edge[0], edge[1]
            graph[a].append(b)
            graph[b].append(a)        

        result = 0

        while graph:
            visited = set()
            start_node = list(graph.keys())[0]
            queue = deque([(start_node, None)])
            visited.add(start_node)

            while queue:
                node, parent = queue.popleft()

                for neighbor in graph[node]:
                    if neighbor not in visited and neighbor != parent:
                        queue.append((neighbor, node))
                        visited.add(neighbor)
            
            for node in visited:
                del graph[node]
            
            result += 1
        
        return result
        
                




