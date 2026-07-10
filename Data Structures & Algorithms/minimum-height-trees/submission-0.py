from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        self.graph = {i: [] for i in range(n)}
        self.indegree = {i: 0 for i in range(n)}

        for edge in edges:
            a, b = edge[0], edge[1]
            self.graph[a].append(b)
            self.indegree[b] += 1
            self.graph[b].append(a)
            self.indegree[a] += 1
        
        heights = []
        for i in range(n):
            height = self.getMinHeight(i)
            heights.append(height)
        
        result = []
        for i in range(n):
            if heights[i] == min(heights):
                result.append(i)
        return result

    def getMinHeight(self, node: int) -> int:
        max_height = 0

        queue = deque([(node, None, 0)])
        visited = set([node])

        while queue:
            node, parent, height = queue.popleft()
            max_height = max(max_height, height)

            for neighbor in self.graph[node]:
                if neighbor not in visited and neighbor != parent:
                    visited.add(neighbor)
                    queue.append((neighbor, parent, height + 1))
        
        return max_height



