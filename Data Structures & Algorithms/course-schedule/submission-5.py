class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degrees = {i:0 for i in range(numCourses)}
        edges = {i: set() for i in range(numCourses)}
        for first, second in prerequisites:
            in_degrees[second] += 1
            edges[first].add(second)
        
        topological_order = []
        
        level = set([node for node in in_degrees.keys() if in_degrees[node] == 0])

        while level:
            next_level = set()
            for node in level:
                dependencies = edges[node]
                for dependency in dependencies:
                    in_degrees[dependency] -= 1
                    if in_degrees[dependency] == 0:
                        next_level.add(dependency)
                del edges[node]
            
            level = next_level
        
        return len(edges) == 0


