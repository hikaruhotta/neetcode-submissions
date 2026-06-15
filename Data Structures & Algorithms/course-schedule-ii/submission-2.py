from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []

        graph = {i: [] for i in range(numCourses)}
        indegrees = {i: 0 for i in range(numCourses)}
        for preq in prerequisites:
            a, b = preq[0], preq[1]
            graph[b].append(a)
            indegrees[a] += 1

        queue = deque()
        
        for course, indegree in indegrees.items():
            if indegree == 0:
                queue.append(course)

        while queue:
            course = queue.popleft()
            result.append(course)

            for neighbor in graph[course]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(result) == numCourses:
            return result
        
        return []
        
