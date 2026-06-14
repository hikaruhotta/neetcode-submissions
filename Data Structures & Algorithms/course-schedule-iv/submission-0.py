from collections import defaultdict, deque

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for preq in prerequisites:
            a, b = preq[0], preq[1]
            adj[a].append(b)
        
        result = []
        for query in queries:
            a, b = query[0], query[1]
            result.append(self.helper(adj, a, b))
        
        return result
    
    def helper(self, adj, a, b):
        queue = deque([a])
        visited = set()

        while queue:
            u = queue.popleft()
            visited.add(u)
            
            if u == b:
                return True
            
            for v in adj[u]:
                if v not in visited:
                    queue.append(v)
        
        return False

