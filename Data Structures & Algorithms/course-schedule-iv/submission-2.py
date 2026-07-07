from collections import deque

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        self.graph = {i: [] for i in range(numCourses)}
        for preq in prerequisites:
            a, b = preq[0], preq[1]
            self.graph[a].append(b)
        results = []
        for query in queries:
            results.append(self.helper(query))
        return results
    
    def helper(self, query: List[int]) -> bool:
        u, v = query[0], query[1]
        queue = deque([u])
        visited = set()
        while queue:
            a = queue.popleft()
            if a in visited:
                continue
            visited.add(a)
            if a == v:
                return True
            
            for b in self.graph[a]:
                if b not in visited:
                    queue.append(b)
        return False

