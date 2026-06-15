from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        indegrees = {i: 0 for i in range(numCourses)}
        for preq in prerequisites:
            a, b = preq[0], preq[1]
            graph[b].append(a)
            indegrees[a] += 1

        queue = deque([])
        for course, indegree in indegrees.items():
            if indegree == 0:
                queue.append(course)
        
        num_processed = 0
        while queue:
            course = queue.popleft()
            for neighbor in graph[course]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
            num_processed += 1
        
        return num_processed == numCourses
        




            
    def zeroIndegreeCourses(self, indegree: dict) -> List[int]:
        results = []
        for course, degree in indegree.items():
            if degree == 0:
                results.append(course)
        return results

        