class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        self.graph = {i: set() for i in range(n)}
        for first, second in edges:
            self.graph[first].add(second)
            self.graph[second].add(first)
        
        self.visited = {i: False for i in range(n)}
        self.parent = {i: -1 for i in range(n)}

        result = self.dfs(0)
        for node, visited in self.visited.items():
            if not visited:
                return False
        
        return result


    def dfs(self, node: int) -> bool:
        self.visited[node] = True

        for adj in self.graph[node]:
            if not self.visited[adj]:
                self.parent[adj] = node
                if not self.dfs(adj):
                    return False
            elif self.parent[node] != adj: # cycle detected
                return False
        
        return True

            