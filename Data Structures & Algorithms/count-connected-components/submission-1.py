class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.visited = {i: False for i in range(n)}
        self.edges = {i: set() for i in range(n)}
        for first, second in edges:
            self.edges[first].add(second)
            self.edges[second].add(first)

        num_components = 0

        while self.getUnvisitedNode() != None:
            unvisited_node = self.getUnvisitedNode()
            self.bfs(unvisited_node)
            num_components += 1
        
        return num_components


    def bfs(self, node) -> None:
        level = set([node])
        while level:
            next_level = set()

            for node in level:
                self.visited[node] = True
                for adj in self.edges[node]:
                    if not self.visited[adj]:
                        next_level.add(adj)
            
            level = next_level


    def getUnvisitedNode(self) -> Optional[int]:
        for node in self.visited.keys():
            if not self.visited[node]:
                return node
        
        return None