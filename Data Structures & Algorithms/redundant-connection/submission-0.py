class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {}
        for a, b in edges:
            if a not in graph:
                graph[a] = set()
            if b not in graph:
                graph[b] = set()
            
            graph[a].add(b)
            graph[b].add(a)

            if self.hasCycle(graph):
                return [a, b]
        
    def hasCycle(self, graph) -> bool:
        visited = {node: False for node in graph.keys()}
        parent = {node: node for node in graph.keys()}
        return not self.dfs(list(graph.keys())[0], graph, visited, parent)

    
    def dfs(self, node, graph, visited, parent) -> bool:
        visited[node] = True

        for adj in graph[node]:
            if not visited[adj]:
                parent[adj] = node
                if not self.dfs(adj, graph, visited, parent):
                    return False
            elif parent[node] != adj:
                    return False
        
        return True
        




            