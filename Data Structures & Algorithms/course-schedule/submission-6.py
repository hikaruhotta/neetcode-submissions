from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        in_degree = [0 for i in range(numCourses)]

        for preq in prerequisites:
            u, v = preq[1], preq[0]
            adj[u].append(v)
            in_degree[v] += 1
        
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        result = []

        while queue:
            node = queue.popleft()
            result.append(node)

            for v in adj[node]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
            
        
        return len(result) == numCourses

        



