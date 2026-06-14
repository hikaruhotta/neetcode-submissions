from collections import defaultdict, deque

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        indegree = [0 for _ in range(numCourses)]
        preq = [set() for _ in range(numCourses)]

        for prerequisite in prerequisites:
            u, v = prerequisite[0], prerequisite[1]
            adj[u].append(v)
            indegree[v] += 1
            preq[v].add(u)
        
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])

        while queue:
            node = queue.popleft()

            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                preq[neighbor].add(node)
                preq[neighbor].update(preq[node])

                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return [u in preq[v] for u, v in queries]
        
                

        


